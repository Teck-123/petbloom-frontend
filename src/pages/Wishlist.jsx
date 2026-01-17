import React from 'react'
import { useNavigate } from 'react-router-dom'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { Heart, ShoppingCart, Trash2 } from 'lucide-react'
import api from '../services/api'
import toast from 'react-hot-toast'

function Wishlist() {
  const navigate = useNavigate()
  const queryClient = useQueryClient()

  const { data: wishlistItems, isLoading } = useQuery({
    queryKey: ['wishlist'],
    queryFn: async () => {
      const response = await api.get('/wishlist')
      return response.data
    }
  })

  const removeFromWishlist = useMutation({
    mutationFn: async (itemId) => {
      await api.delete(`/wishlist/${itemId}`)
    },
    onSuccess: () => {
      queryClient.invalidateQueries(['wishlist'])
      toast.success('Removed from wishlist')
    }
  })

  const addToCart = useMutation({
    mutationFn: async (item) => {
      const productId = item.productId
      const petId = item.petId
      await api.post('/cart', { productId, petId, quantity: 1 })
    },
    onSuccess: () => {
      toast.success('Added to cart!')
    },
    onError: (error) => {
      toast.error(error.response?.data?.detail || 'Failed to add to cart')
    }
  })

  const clearWishlist = useMutation({
    mutationFn: async () => {
      await api.delete('/wishlist')
    },
    onSuccess: () => {
      queryClient.invalidateQueries(['wishlist'])
      toast.success('Wishlist cleared')
    }
  })

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500"></div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex items-center justify-between mb-8">
          <div className="flex items-center">
            <Heart className="h-8 w-8 text-primary-500 mr-3" />
            <h1 className="text-3xl font-bold text-gray-900">My Wishlist</h1>
          </div>
          {wishlistItems?.length > 0 && (
            <button
              onClick={() => clearWishlist.mutate()}
              className="text-red-500 hover:text-red-600 text-sm font-medium flex items-center"
            >
              <Trash2 className="h-4 w-4 mr-1" />
              Clear All
            </button>
          )}
        </div>

        {wishlistItems?.length === 0 ? (
          <div className="bg-white rounded-lg shadow-md p-12 text-center">
            <Heart className="h-16 w-16 text-gray-400 mx-auto mb-4" />
            <h2 className="text-2xl font-semibold text-gray-900 mb-2">Your wishlist is empty</h2>
            <p className="text-gray-600 mb-6">Add some adorable pets or premium supplies to your wishlist!</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button
                onClick={() => navigate('/pets')}
                className="btn-primary"
              >
                Browse Pets
              </button>
              <button
                onClick={() => navigate('/products')}
                className="btn-outline"
              >
                Shop Supplies
              </button>
            </div>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {wishlistItems?.map((item) => {
              const product = item.product
              const pet = item.pet
              const itemData = product || pet
              const name = product ? product.name : (pet ? pet.name : 'Unknown')
              const price = product ? product.price : (pet ? pet.adoptionFee : 0)
              const image = product ? product.images?.[0] : (pet ? pet.images?.[0] : '')
              const description = product 
                ? `${product.brand} • ${product.category.replace('_', ' ')}`
                : (pet ? `${pet.breed} • ${pet.age} years old` : '')

              return (
                <div key={item.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
                  <div className="relative">
                    <img
                      src={image || '/placeholder.jpg'}
                      alt={name}
                      className="w-full h-48 object-cover"
                    />
                    <button
                      onClick={() => removeFromWishlist.mutate(item.id)}
                      className="absolute top-2 right-2 p-2 bg-white rounded-full shadow-md hover:bg-gray-50 transition-colors"
                    >
                      <Trash2 className="h-4 w-4 text-red-500" />
                    </button>
                  </div>
                  <div className="p-4">
                    <h3 className="text-lg font-semibold text-gray-900 mb-1">{name}</h3>
                    <p className="text-sm text-gray-600 mb-2">{description}</p>
                    <p className="text-xl font-bold text-primary-500 mb-4">${price}</p>
                    <div className="flex space-x-2">
                      <button
                        onClick={() => navigate(product ? `/products/${product.id}` : `/pets/${pet.id}`)}
                        className="flex-1 bg-gray-100 text-gray-700 text-center py-2 rounded-md text-sm font-medium hover:bg-gray-200 transition-colors"
                      >
                        View Details
                      </button>
                      <button
                        onClick={() => addToCart.mutate(item)}
                        className="flex-1 btn-primary flex items-center justify-center text-sm"
                      >
                        <ShoppingCart className="h-4 w-4 mr-1" />
                        Add to Cart
                      </button>
                    </div>
                  </div>
                </div>
              )
            })}
          </div>
        )}
      </div>
    </div>
  )
}

export default Wishlist