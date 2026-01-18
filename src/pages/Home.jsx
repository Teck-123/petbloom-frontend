import React from 'react'
import { Link } from 'react-router-dom'
import { 
  PawPrint, 
  Heart, 
  ShoppingCart, 
  Shield, 
  Truck, 
  Users,
  ArrowRight,
  Star
} from 'lucide-react'
import { useQuery } from '@tanstack/react-query'
import api from '../services/api'

function Home() {
  // Fetch featured pets
  const { data: featuredPets, isLoading: petsLoading } = useQuery({
    queryKey: ['featuredPets'],
    queryFn: async () => {
      const response = await api.get('/pets?limit=6')
      return response.data.data || response.data
    }
  })

  // Fetch featured products
  const { data: featuredProducts, isLoading: productsLoading } = useQuery({
    queryKey: ['featuredProducts'],
    queryFn: async () => {
      const response = await api.get('/products?limit=6')
      return response.data.data || response.data
    }
  })

  const features = [
    {
      icon: Shield,
      title: 'Verified Breeders',
      description: 'All our breeders are thoroughly vetted and verified for your peace of mind.'
    },
    {
      icon: Heart,
      title: 'Healthy Pets',
      description: 'Every pet comes with health records and is examined by veterinarians.'
    },
    {
      icon: Truck,
      title: 'Safe Delivery',
      description: 'We ensure safe and comfortable transportation for your new family member.'
    },
    {
      icon: Users,
      title: 'Expert Support',
      description: 'Our pet experts are here to help you every step of the way.'
    }
  ]

  const testimonials = [
    {
      name: 'Sarah Johnson',
      location: 'New York',
      comment: 'Found the perfect Golden Retriever puppy through PetBloom. The process was smooth and our new family member is healthy and happy!',
      rating: 5
    },
    {
      name: 'Mike Chen',
      location: 'California',
      comment: 'Excellent service! The breeder was professional and the pet supplies recommendation helped us prepare perfectly.',
      rating: 5
    },
    {
      name: 'Emily Rodriguez',
      location: 'Texas',
      comment: 'Adopted a rescue cat and couldn\'t be happier. PetBloom made the adoption process so easy and stress-free.',
      rating: 5
    }
  ]

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-primary-50 to-secondary-50 py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h1 className="text-4xl lg:text-6xl font-bold text-gray-900 mb-6">
                Find Your Perfect 
                <span className="text-primary-500">Companion</span>
              </h1>
              <p className="text-xl text-gray-600 mb-8">
                Discover healthy, loving pets from verified breeders and shelters. 
                Everything you need for your new family member in one convenient place.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Link
                  to="/pets"
                  className="bg-primary-500 text-white px-8 py-3 rounded-lg font-medium hover:bg-primary-600 transition-colors flex items-center justify-center"
                >
                  Browse Pets
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Link>
                <Link
                  to="/products"
                  className="border border-primary-500 text-primary-500 px-8 py-3 rounded-lg font-medium hover:bg-primary-50 transition-colors flex items-center justify-center"
                >
                  Shop Supplies
                </Link>
              </div>
            </div>
            <div className="relative">
              <div className="bg-white rounded-2xl shadow-xl p-8">
                <div className="grid grid-cols-2 gap-4">
                  <div className="bg-primary-100 rounded-lg p-4 text-center">
                    <PawPrint className="h-12 w-12 text-primary-500 mx-auto mb-2" />
                    <p className="text-sm font-medium text-gray-700">1000+ Happy Pets</p>
                  </div>
                  <div className="bg-secondary-100 rounded-lg p-4 text-center">
                    <Heart className="h-12 w-12 text-secondary-500 mx-auto mb-2" />
                    <p className="text-sm font-medium text-gray-700">500+ Families</p>
                  </div>
                  <div className="bg-accent-100 rounded-lg p-4 text-center">
                    <ShoppingCart className="h-12 w-12 text-accent-500 mx-auto mb-2" />
                    <p className="text-sm font-medium text-gray-700">Premium Supplies</p>
                  </div>
                  <div className="bg-green-100 rounded-lg p-4 text-center">
                    <Shield className="h-12 w-12 text-green-500 mx-auto mb-2" />
                    <p className="text-sm font-medium text-gray-700">Verified Breeders</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Why Choose PetBloom?</h2>
            <p className="text-lg text-gray-600">We make pet adoption and care simple, safe, and joyful</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <div key={index} className="text-center">
                <div className="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                  <feature.icon className="h-8 w-8 text-primary-500" />
                </div>
                <h3 className="text-lg font-semibold text-gray-900 mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Pets Section */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center mb-12">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-4">Featured Pets</h2>
              <p className="text-lg text-gray-600">Meet some of our adorable companions looking for their forever homes</p>
            </div>
            <Link
              to="/pets"
              className="text-primary-500 hover:text-primary-600 font-medium flex items-center"
            >
              View All
              <ArrowRight className="ml-1 h-4 w-4" />
            </Link>
          </div>
          
          {petsLoading ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {[1, 2, 3].map((i) => (
                <div key={i} className="animate-pulse">
                  <div className="bg-gray-300 h-64 rounded-lg mb-4"></div>
                  <div className="bg-gray-300 h-4 rounded mb-2"></div>
                  <div className="bg-gray-300 h-4 rounded w-3/4"></div>
                </div>
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {featuredPets?.map((pet) => (
                <div key={pet.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
                  <img
                    src={pet.images?.[0] || '/placeholder-pet.jpg'}
                    alt={pet.name}
                    className="w-full h-64 object-cover"
                  />
                  <div className="p-6">
                    <h3 className="text-xl font-semibold text-gray-900 mb-2">{pet.name}</h3>
                    <p className="text-gray-600 mb-2">{pet.breed} • {pet.age} years old</p>
                    <p className="text-lg font-bold text-primary-500 mb-4">${pet.price}</p>
                    <Link
                      to={`/pets/${pet.id}`}
                      className="w-full bg-primary-500 text-white text-center py-2 rounded-md hover:bg-primary-600 transition-colors block"
                    >
                      View Details
                    </Link>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </section>

      {/* Featured Products Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center mb-12">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-4">Popular Supplies</h2>
              <p className="text-lg text-gray-600">Everything your pet needs for a happy, healthy life</p>
            </div>
            <Link
              to="/products"
              className="text-primary-500 hover:text-primary-600 font-medium flex items-center"
            >
              Shop All
              <ArrowRight className="ml-1 h-4 w-4" />
            </Link>
          </div>
          
          {productsLoading ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {[1, 2, 3].map((i) => (
                <div key={i} className="animate-pulse">
                  <div className="bg-gray-300 h-64 rounded-lg mb-4"></div>
                  <div className="bg-gray-300 h-4 rounded mb-2"></div>
                  <div className="bg-gray-300 h-4 rounded w-3/4"></div>
                </div>
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {featuredProducts?.map((product) => (
                <div key={product.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
                  <img
                    src={product.images?.[0] || '/placeholder-product.jpg'}
                    alt={product.name}
                    className="w-full h-64 object-cover"
                  />
                  <div className="p-6">
                    <h3 className="text-xl font-semibold text-gray-900 mb-2">{product.name}</h3>
                    <p className="text-gray-600 mb-2">{product.brand} • {product.category}</p>
                    <p className="text-lg font-bold text-primary-500 mb-4">${product.price}</p>
                    <Link
                      to={`/products/${product.id}`}
                      className="w-full bg-primary-500 text-white text-center py-2 rounded-md hover:bg-primary-600 transition-colors block"
                    >
                      View Product
                    </Link>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">What Our Customers Say</h2>
            <p className="text-lg text-gray-600">Real stories from happy pet parents</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <div key={index} className="bg-white rounded-lg shadow-md p-6">
                <div className="flex mb-4">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <Star key={i} className="h-5 w-5 text-yellow-400 fill-current" />
                  ))}
                </div>
                <p className="text-gray-600 mb-4">"{testimonial.comment}"</p>
                <div>
                  <p className="font-semibold text-gray-900">{testimonial.name}</p>
                  <p className="text-sm text-gray-500">{testimonial.location}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-primary-500">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl font-bold text-white mb-4">
            Ready to Find Your Perfect Companion?
          </h2>
          <p className="text-xl text-primary-100 mb-8">
            Join thousands of happy families who found their furry friends through PetBloom
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              to="/pets"
              className="bg-white text-primary-500 px-8 py-3 rounded-lg font-medium hover:bg-gray-100 transition-colors"
            >
              Browse Available Pets
            </Link>
            <Link
              to="/register"
              className="border-2 border-white text-white px-8 py-3 rounded-lg font-medium hover:bg-white hover:text-primary-500 transition-colors"
            >
              Create Account
            </Link>
          </div>
        </div>
      </section>
    </div>
  )
}

export default Home