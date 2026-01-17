import React from 'react'
import { useNavigate } from 'react-router-dom'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { 
  ShoppingCart, 
  Trash2, 
  Plus, 
  Minus,
  Heart,
  ArrowRight
} from 'lucide-react'
import api from '../services/api'
import toast from 'react-hot-toast'

function Cart() {
  const navigate = useNavigate()
  const queryClient = useQueryClient()

  // Fetch cart items
  const { data: cartItems, isLoading } = useQuery({
    queryKey: ['cart'],
    queryFn: async () => {
      const response = await api.get('/cart')
      return response.data
    }
  })

  // Update cart item mutation
  const updateCartItem = useMutation({
    mutationFn: async ({ itemId, quantity }) => {
      const response = await api.put(`/cart/${itemId}`, { quantity })
      return response.data
    },
    onSuccess: () => {
      queryClient.invalidateQueries(['cart'])
    }
  })

  // Remove cart item mutation
  const removeCartItem = useMutation({
    mutationFn: async (itemId) => {
      await api.delete(`/cart/${itemId}`)
    },
    onSuccess: () => {
      queryClient.invalidateQueries(['cart'])
      toast.success('Item removed from cart')
    }
  })

  // Clear cart mutation
  const clearCart = useMutation({
    mutationFn: async () => {
      await api.delete('/cart')
    },
    onSuccess: () => {
      queryClient.invalidateQueries(['cart'])
      toast.success('Cart cleared')
    }
  })

  const handleQuantityChange = (itemId, newQuantity) => {
    if (newQuantity < 1) {
      removeCartItem.mutate(itemId)
    } else {
      updateCartItem.mutate({ itemId, quantity: newQuantity })
    }
  }

  const calculateTotal = () => {
    if (!cartItems) return 0
    return cartItems.reduce((total, item) => {
      const price = item.product ? item.product.price : (item.pet ? item.pet.adoptionFee : 0)
      return total + (price * item.quantity)
    }, 0)
  }

  const calculateTax = () => {
    return calculateTotal() * 0.08 // 8% tax
  }

  const calculateFinalTotal = () => {
    return calculateTotal() + calculateTax()
  }

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
        <div className="flex items-center mb-8">
          <ShoppingCart className="h-8 w-8 text-primary-500 mr-3" />
          <h1 className="text-3xl font-bold text-gray-900">Shopping Cart</h1>
        </div>

        {cartItems?.length === 0 ? (
          <div className="bg-white rounded-lg shadow-md p-12 text-center">
            <ShoppingCart className="h-16 w-16 text-gray-400 mx-auto mb-4" />
            <h2 className="text-2xl font-semibold text-gray-900 mb-2">Your cart is empty</h2>
            <p className="text-gray-600 mb-6">Add some adorable pets or premium supplies to get started!</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button
                onClick={() => navigate('/pets')}
                className="btn-primary flex items-center justify-center"
              >
                Browse Pets
              </button>
              <button
                onClick={() => navigate('/products')}
                className="btn-outline flex items-center justify-center"
              >
                Shop Supplies
              </button>
            </div>
          </div>
        ) : (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {/* Cart Items */}
            <div className="lg:col-span-2">
              <div className="bg-white rounded-lg shadow-md">
                <div className="p-6 border-b border-gray-200 flex justify-between items-center">
                  <h2 className="text-xl font-semibold text-gray-900">
                    Cart Items ({cartItems?.length || 0})
                  </h2>
                  <button
                    onClick={() => clearCart.mutate()}
                    className="text-red-500 hover:text-red-600 text-sm font-medium flex items-center"
                  >
                    <Trash2 className="h-4 w-4 mr-1" />
                    Clear Cart
                  </button>
                </div>
                
                <div className="divide-y divide-gray-200">
                  {cartItems?.map((item) => {
                    const product = item.product
                    const pet = item.pet
                    const itemData = product || pet
                    const price = product ? product.price : (pet ? pet.adoptionFee : 0)
                    const image = product ? product.images?.[0] : (pet ? pet.images?.[0] : '')
                    const name = product ? product.name : (pet ? pet.name : 'Unknown')
                    const description = product 
                      ? `${product.brand} • ${product.category.replace('_', ' ')}`
                      : (pet ? `${pet.breed} • ${pet.age} years old` : '')

                    return (
                      <div key={item.id} className="p-6">
                        <div className="flex items-center space-x-4">
                          <div className="flex-shrink-0">
                            <img
                              src={image || '/placeholder.jpg'}
                              alt={name}
                              className="w-20 h-20 object-cover rounded-md"
                            />
                          </div>
                          
                          <div className="flex-1">
                            <h3 className="text-lg font-semibold text-gray-900 mb-1">{name}</h3>
                            <p className="text-sm text-gray-600 mb-2">{description}</p>
                            <p className="text-xl font-bold text-primary-500">${price}</p>
                          </div>
                          
                          <div className="flex flex-col items-end space-y-2">
                            {/* Quantity Controls */}
                            <div className="flex items-center space-x-2">
                              <button
                                onClick={() => handleQuantityChange(item.id, item.quantity - 1)}
                                className="p-1 border border-gray-300 rounded hover:bg-gray-50"
                              >
                                <Minus className="h-4 w-4" />
                              </button>
                              <span className="w-12 text-center font-medium">{item.quantity}</span>
                              <button
                                onClick={() => handleQuantityChange(item.id, item.quantity + 1)}
                                className="p-1 border border-gray-300 rounded hover:bg-gray-50"
                                disabled={product && item.quantity >= product.stock}
                              >
                                <Plus className="h-4 w-4" />
                              </button>
                            </div>
                            
                            {/* Actions */}
                            <div className="flex items-center space-x-2">
                              <button
                                onClick={() => handleAddToWishlist(product ? product.id : pet.id)}
                                className="p-2 text-gray-400 hover:text-red-500 transition-colors"
                              >
                                <Heart className="h-4 w-4" />
                              </button>
                              <button
                                onClick={() => removeCartItem.mutate(item.id)}
                                className="p-2 text-gray-400 hover:text-red-500 transition-colors"
                              >
                                <Trash2 className="h-4 w-4" />
                              </button>
                            </div>
                            
                            {/* Item Total */}
                            <p className="text-sm font-medium text-gray-900">
                              Subtotal: ${(price * item.quantity).toFixed(2)}
                            </p>
                          </div>
                        </div>
                      </div>
                    )
                  })}
                </div>
              </div>
            </div>

            {/* Order Summary */}
            <div className="lg:col-span-1">
              <div className="bg-white rounded-lg shadow-md p-6 sticky top-24">
                <h2 className="text-xl font-semibold text-gray-900 mb-4">Order Summary</h2>
                
                <div className="space-y-3 mb-6">
                  <div className="flex justify-between">
                    <span className="text-gray-600">Subtotal</span>
                    <span className="font-medium">${calculateTotal().toFixed(2)}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-600">Tax</span>
                    <span className="font-medium">${calculateTax().toFixed(2)}</span>
                  </div>
                  <div className="border-t border-gray-200 pt-3">
                    <div className="flex justify-between">
                      <span className="text-lg font-semibold text-gray-900">Total</span>
                      <span className="text-lg font-bold text-primary-500">
                        ${calculateFinalTotal().toFixed(2)}
                      </span>
                    </div>
                  </div>
                </div>

                <button
                  onClick={() => navigate('/checkout')}
                  className="w-full btn-primary flex items-center justify-center mb-3"
                >
                  Proceed to Checkout
                  <ArrowRight className="ml-2 h-5 w-5" />
                </button>
                
                <button
                  onClick={() => navigate('/products')}
                  className="w-full btn-outline"
                >
                  Continue Shopping
                </button>

                {/* Security Badges */}
                <div className="mt-6 pt-6 border-t border-gray-200">
                  <div className="flex items-center justify-center space-x-4 text-sm text-gray-600">
                    <div className="flex items-center">
                      <Check className="h-4 w-4 text-green-500 mr-1" />
                      Secure Checkout
                    </div>
                    <div className="flex items-center">
                      <Check className="h-4 w-4 text-green-500 mr-1" />
                      SSL Protected
                    </div>
                  </div>
                </div>
              </div>

              {/* Why Shop With Us */}
              <div className="bg-white rounded-lg shadow-md p-6 mt-6">
                <h3 className="text-lg font-semibold text-gray-900 mb-4">Why Shop With Us?</h3>
                <div className="space-y-3">
                  <div className="flex items-center text-sm text-gray-600">
                    <Check className="h-4 w-4 text-green-500 mr-2 flex-shrink-0" />
                    Free shipping on orders over $50
                  </div>
                  <div className="flex items-center text-sm text-gray-600">
                    <Check className="h-4 w-4 text-green-500 mr-2 flex-shrink-0" />
                    30-day money-back guarantee
                  </div>
                  <div className="flex items-center text-sm text-gray-600">
                    <Check className="h-4 w-4 text-green-500 mr-2 flex-shrink-0" />
                    Verified breeders and quality products
                  </div>
                  <div className="flex items-center text-sm text-gray-600">
                    <Check className="h-4 w-4 text-green-500 mr-2 flex-shrink-0" />
                    Expert customer support
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default Cart