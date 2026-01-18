import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import {
  ArrowLeft,
  Heart,
  ShoppingCart,
  Phone,
  Mail,
  MapPin,
  Check,
  Star,
  Calendar,
  Ruler,
  Palette,
  PawPrint
} from 'lucide-react'
import api from '../services/api'
import toast from 'react-hot-toast'
import { useAuth } from '../contexts/AuthContext'

function PetDetail() {
  const { id } = useParams()
  const navigate = useNavigate()
  const { currentUser } = useAuth()
  const [selectedImage, setSelectedImage] = useState(0)

  // Fetch pet details
  const { data: pet, isLoading, error } = useQuery({
    queryKey: ['pet', id],
    queryFn: async () => {
      const response = await api.get(`/pets/${id}`)
      return response.data
    }
  })

  const handleAddToCart = async () => {
    if (!currentUser) {
      toast.error('Please login to add pets to cart')
      navigate('/login')
      return
    }

    try {
      await api.post('/cart', { petId: id, quantity: 1 })
      toast.success('Added to cart!')
    } catch (error) {
      toast.error(error.response?.data?.detail || 'Failed to add to cart')
    }
  }

  const handleAddToWishlist = async () => {
    if (!currentUser) {
      toast.error('Please login to add pets to wishlist')
      navigate('/login')
      return
    }

    try {
      await api.post('/wishlist', { petId: id })
      toast.success('Added to wishlist!')
    } catch (error) {
      toast.error(error.response?.data?.detail || 'Failed to add to wishlist')
    }
  }

  const handleContactBreeder = () => {
    if (!currentUser) {
      toast.error('Please login to contact breeder')
      navigate('/login')
      return
    }
    // In a real app, this would open a contact form or chat
    toast.success('Contact information will be shared via email')
  }

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500"></div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-2">Pet Not Found</h2>
          <p className="text-gray-600 mb-4">The pet you're looking for doesn't exist or has been adopted.</p>
          <button
            onClick={() => navigate('/pets')}
            className="btn-primary flex items-center mx-auto"
          >
            <ArrowLeft className="mr-2 h-4 w-4" />
            Back to Pets
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Back Button */}
        <button
          onClick={() => navigate(-1)}
          className="flex items-center text-gray-600 hover:text-gray-900 mb-6"
        >
          <ArrowLeft className="mr-2 h-5 w-5" />
          Back
        </button>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Image Gallery */}
          <div>
            <div className="bg-white rounded-lg shadow-md overflow-hidden mb-4">
              <img
                src={pet?.images?.[selectedImage] || '/placeholder-pet.jpg'}
                alt={pet?.name}
                className="w-full h-96 object-cover"
              />
            </div>

            {/* Thumbnail Images */}
            {pet?.images && pet.images.length > 1 && (
              <div className="flex space-x-2 overflow-x-auto">
                {pet.images.map((image, index) => (
                  <button
                    key={index}
                    onClick={() => setSelectedImage(index)}
                    className={`flex-shrink-0 w-20 h-20 rounded-md overflow-hidden border-2 ${selectedImage === index ? 'border-primary-500' : 'border-gray-300'
                      }`}
                  >
                    <img
                      src={image}
                      alt={`${pet.name} ${index + 1}`}
                      className="w-full h-full object-cover"
                    />
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Pet Information */}
          <div>
            <div className="bg-white rounded-lg shadow-md p-6 mb-6">
              <div className="flex items-start justify-between mb-4">
                <div>
                  <h1 className="text-3xl font-bold text-gray-900 mb-2">{pet?.name}</h1>
                  <p className="text-lg text-gray-600">
                    {pet?.breed} • {pet?.age} year{pet?.age !== 1 ? 's' : ''} old • {pet?.gender}
                  </p>
                </div>
                <button
                  onClick={handleAddToWishlist}
                  className="p-2 border border-gray-300 rounded-full hover:bg-gray-50 transition-colors"
                >
                  <Heart className="h-6 w-6 text-gray-600" />
                </button>
              </div>

              <div className="mb-6">
                <p className="text-3xl font-bold text-primary-500 mb-4">${pet?.adoptionFee}</p>

                <div className="flex flex-col sm:flex-row gap-4">
                  <button
                    onClick={handleAddToCart}
                    className="btn-primary flex-1 flex items-center justify-center"
                  >
                    <ShoppingCart className="mr-2 h-5 w-5" />
                    Add to Cart
                  </button>
                  <button
                    onClick={handleContactBreeder}
                    className="btn-outline flex-1 flex items-center justify-center"
                  >
                    Contact Breeder
                  </button>
                </div>
              </div>

              {/* Pet Details */}
              <div className="space-y-4">
                <h2 className="text-xl font-semibold text-gray-900">About {pet?.name}</h2>
                <p className="text-gray-700 leading-relaxed">{pet?.description}</p>
              </div>
            </div>

            {/* Pet Information Cards */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
              <div className="bg-white rounded-lg shadow-md p-4">
                <div className="flex items-center mb-2">
                  <Calendar className="h-5 w-5 text-primary-500 mr-2" />
                  <h3 className="font-semibold text-gray-900">Age</h3>
                </div>
                <p className="text-gray-700">{pet?.age} year{pet?.age !== 1 ? 's' : ''} old</p>
              </div>

              <div className="bg-white rounded-lg shadow-md p-4">
                <div className="flex items-center mb-2">
                  <Ruler className="h-5 w-5 text-primary-500 mr-2" />
                  <h3 className="font-semibold text-gray-900">Size</h3>
                </div>
                <p className="text-gray-700 capitalize">{pet?.size}</p>
              </div>

              <div className="bg-white rounded-lg shadow-md p-4">
                <div className="flex items-center mb-2">
                  <PawPrint className="h-5 w-5 text-primary-500 mr-2" />
                  <h3 className="font-semibold text-gray-900">Breed</h3>
                </div>
                <p className="text-gray-700">{pet?.breed}</p>
              </div>

              <div className="bg-white rounded-lg shadow-md p-4">
                <div className="flex items-center mb-2">
                  <Palette className="h-5 w-5 text-primary-500 mr-2" />
                  <h3 className="font-semibold text-gray-900">Color</h3>
                </div>
                <p className="text-gray-700">{pet?.color}</p>
              </div>
            </div>

            {/* Health Information */}
            <div className="bg-white rounded-lg shadow-md p-6 mb-6">
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Health & Temperament</h2>
              <div className="space-y-3">
                <div className="flex items-center">
                  <Check className="h-5 w-5 text-green-500 mr-3" />
                  <span className="text-gray-700">Health Status: {pet?.healthStatus}</span>
                </div>
                <div className="flex items-center">
                  <Check className="h-5 w-5 text-green-500 mr-3" />
                  <span className="text-gray-700">Temperament: {pet?.temperament}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Breeder Information */}
        <div className="mt-8 bg-white rounded-lg shadow-md p-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Breeder Information</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">{pet?.breeder?.name}</h3>
              <div className="space-y-2 text-gray-600">
                <div className="flex items-center">
                  <Star className="h-4 w-4 text-yellow-400 mr-2" />
                  <span>{pet?.breeder?.rating}/5.0 Rating</span>
                </div>
                <div className="flex items-center">
                  <MapPin className="h-4 w-4 text-gray-400 mr-2" />
                  <span>{pet?.breeder?.city}, {pet?.breeder?.state}</span>
                </div>
              </div>
              <p className="mt-3 text-gray-700">{pet?.breeder?.description}</p>
            </div>

            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">Contact Information</h3>
              <div className="space-y-3">
                <div className="flex items-center">
                  <Phone className="h-5 w-5 text-primary-500 mr-3" />
                  <span className="text-gray-700">{pet?.breeder?.phone}</span>
                </div>
                <div className="flex items-center">
                  <Mail className="h-5 w-5 text-primary-500 mr-3" />
                  <span className="text-gray-700">{pet?.breeder?.email}</span>
                </div>
                <div className="flex items-center">
                  <MapPin className="h-5 w-5 text-primary-500 mr-3" />
                  <span className="text-gray-700">{pet?.breeder?.address}</span>
                </div>
              </div>

              <button
                onClick={handleContactBreeder}
                className="mt-4 btn-outline w-full"
              >
                Contact Breeder
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default PetDetail