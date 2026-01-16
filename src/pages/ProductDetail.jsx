import React from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { ArrowLeft, Heart, ShoppingCart, Star, Truck, Shield } from 'lucide-react'
import api from '../services/api'
import toast from 'react-hot-toast'
import { useAuth } from '../contexts/AuthContext'

function ProductDetail() {
  const { id } = useParams()
  const navigate = useNavigate()
  const { currentUser } = useAuth()

  const { data: product, isLoading, error } = useQuery({
    queryKey: ['product', id],
    queryFn: async () => {
      const response = await api.get(`/products/${id}`)
      return response.data
    }
  })

  const handleAddToCart = async () => {
    if (!currentUser) {
      toast.error('Please login to add items to cart')
      navigate('/login')
      return
    }

    try {
      await api.post('/cart', { productId: id, quantity: 1 })
      toast.success('Added to cart!')
    } catch (error) {
      toast.error(error.response?.data?.detail || 'Failed to add to cart')
    }
  }

  const handleAddToWishlist = async () => {
    if (!currentUser) {
      toast.error('Please login to add items to wishlist')
      navigate('/login')
      return
    }

    try {
      await api.post('/wishlist', { productId: id })
      toast.success('Added to wishlist!')
    } catch (error) {
      toast.error(error.response?.data?.detail || 'Failed to add to wishlist')
    }
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
          <h2 className="text-2xl font-bold text-gray-900 mb-2">Product Not Found</h2>
          <p className="text-gray-600 mb-4">The product you're looking for doesn't exist.</p>
          <button
            onClick={() => navigate('/products')}
            className="btn-primary flex items-center mx-auto"
          >
            <ArrowLeft className="mr-2 h-4 w-4" />
            Back to Products
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <button
          onClick={() => navigate(-1)}
          className="flex items-center text-gray-600 hover:text-gray-900 mb-6"
        >
          <ArrowLeft className="mr-2 h-5 w-5" />
          Back
        </button>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Product Images */}
          <div>
            <div className="bg-white rounded-lg shadow-md overflow-hidden mb-4">
              <img
                src={product?.images?.[0] || '/placeholder-product.jpg'}
                alt={product?.name}
                className="w-full h-96 object-cover"
              />
            </div>
          </div>

          {/* Product Information */}
          <div>
            <div className="bg-white rounded-lg shadow-md p-6 mb-6">
              <div className="flex items-start justify-between mb-4">
                <div>
                  <h1 className="text-3xl font-bold text-gray-900 mb-2">{product?.name}</h1>
                  <p className="text-lg text-gray-600 mb-2">
                    {product?.brand} • {product?.category.replace('_', ' ')}
                  </p>
                  <div className="flex items-center mb-4">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="h-5 w-5 text-yellow-400 fill-current" />
                    ))}
                    <span className="ml-2 text-gray-600">(4.0) • 23 reviews</span>
                  </div>
                </div>
                <button
                  onClick={handleAddToWishlist}
                  className="p-2 border border-gray-300 rounded-full hover:bg-gray-50 transition-colors"
                >
                  <Heart className="h-6 w-6 text-gray-600" />
                </button>
              </div>

              <div className="mb-6">
                <p className="text-3xl font-bold text-primary-500 mb-4">${product?.price}</p>
                
                <div className="flex items-center mb-4">
                  <span className="text-sm text-gray-600 mr-4">
                    {product?.stock > 0 ? `${product?.stock} in stock` : 'Out of stock'}
                  </span>
                  {product?.stock <= 5 && product?.stock > 0 && (
                    <span className="text-sm text-red-500 font-medium">
                      Only {product?.stock} left!
                    </span>
                  )}
                </div>

                <div className="flex space-x-4">
                  <button
                    onClick={handleAddToCart}
                    disabled={product?.stock === 0}
                    className="btn-primary flex-1 flex items-center justify-center disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    <ShoppingCart className="mr-2 h-5 w-5" />
                    Add to Cart
                  </button>
                  <button className="btn-outline flex-1">
                    Buy Now
                  </button>
                </div>
              </div>

              <div className="space-y-4">
                <h2 className="text-xl font-semibold text-gray-900">Description</h2>
                <p className="text-gray-700 leading-relaxed">{product?.description}</p>
              </div>
            </div>

            {/* Product Features */}
            <div className="bg-white rounded-lg shadow-md p-6 mb-6">
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Product Details</h2>
              <div className="space-y-3">
                <div className="flex justify-between">
                  <span className="text-gray-600">Brand</span>
                  <span className="font-medium">{product?.brand}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Category</span>
                  <span className="font-medium">{product?.category.replace('_', ' ')}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">For Pets</span>
                  <span className="font-medium">{product?.petType?.join(', ')}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProductDetail