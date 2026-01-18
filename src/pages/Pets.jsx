import React, { useState } from 'react'
import { Link, useSearchParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { 
  PawPrint, 
  Filter, 
  Search, 
  Heart,
  ChevronLeft,
  ChevronRight
} from 'lucide-react'
import api from '../services/api'
import toast from 'react-hot-toast'

function Pets() {
  const [searchParams, setSearchParams] = useSearchParams()
  const [searchQuery, setSearchQuery] = useState(searchParams.get('search') || '')
  
  // Pagination state
  const [currentPage, setCurrentPage] = useState(1)
  const itemsPerPage = 12

  // Filters state
  const [filters, setFilters] = useState({
    species: searchParams.get('species') || '',
    breed: searchParams.get('breed') || '',
    size: searchParams.get('size') || '',
    minPrice: searchParams.get('minPrice') || '',
    maxPrice: searchParams.get('maxPrice') || ''
  })

  // Fetch pets
  const { data: petsData, isLoading, error } = useQuery({
    queryKey: ['pets', currentPage, filters, searchQuery],
    queryFn: async () => {
      const params = new URLSearchParams({
        skip: (currentPage - 1) * itemsPerPage,
        limit: itemsPerPage,
        ...Object.fromEntries(Object.entries(filters).filter(([_, v]) => v)),
        ...(searchQuery && { search: searchQuery })
      })
      
      const response = await api.get(`/pets?${params}`)
      return response.data
    }
  })

  // Fetch species and breeds for filters
  const { data: speciesList } = useQuery({
    queryKey: ['species'],
    queryFn: async () => {
      const response = await api.get('/pets/species/list')
      return response.data
    }
  })

  const { data: breedsList } = useQuery({
    queryKey: ['breeds', filters.species],
    queryFn: async () => {
      if (!filters.species) return []
      const response = await api.get(`/pets/breeds/${filters.species}`)
      return response.data
    },
    enabled: !!filters.species
  })

  const handleFilterChange = (key, value) => {
    setFilters(prev => ({ ...prev, [key]: value }))
    setCurrentPage(1)
  }

  const handleSearch = (e) => {
    e.preventDefault()
    setCurrentPage(1)
  }

  const handleAddToWishlist = async (petId) => {
    try {
      await api.post('/wishlist', { petId })
      toast.success('Added to wishlist!')
    } catch (error) {
      if (error.response?.status === 401) {
        toast.error('Please login to add items to wishlist')
      } else {
        toast.error(error.response?.data?.detail || 'Failed to add to wishlist')
      }
    }
  }

  const totalPages = petsData ? Math.ceil(petsData.total / itemsPerPage) : 0

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <PawPrint className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-gray-900 mb-2">Oops! Something went wrong</h2>
          <p className="text-gray-600 mb-4">Failed to load pets. Please try again.</p>
          <button 
            onClick={() => window.location.reload()}
            className="btn-primary"
          >
            Try Again
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Find Your Perfect Companion</h1>
          <p className="text-gray-600">Browse our collection of adorable pets from verified breeders</p>
        </div>

        <div className="flex flex-col lg:flex-row gap-8">
          {/* Filters Sidebar */}
          <div className="lg:w-1/4">
            <div className="bg-white rounded-lg shadow-md p-6 sticky top-24">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-lg font-semibold text-gray-900 flex items-center">
                  <Filter className="h-5 w-5 mr-2" />
                  Filters
                </h2>
                <button
                  onClick={() => {
                    setFilters({
                      species: '',
                      breed: '',
                      size: '',
                      minPrice: '',
                      maxPrice: ''
                    })
                    setSearchQuery('')
                  }}
                  className="text-sm text-primary-500 hover:text-primary-600"
                >
                  Clear All
                </button>
              </div>

              {/* Search */}
              <form onSubmit={handleSearch} className="mb-6">
                <div className="relative">
                  <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
                  <input
                    type="text"
                    placeholder="Search pets..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                  />
                </div>
              </form>

              {/* Species Filter */}
              <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Species</label>
                <select
                  value={filters.species}
                  onChange={(e) => handleFilterChange('species', e.target.value)}
                  className="select w-full"
                >
                  <option value="">All Species</option>
                  {speciesList?.map((species) => (
                    <option key={species} value={species}>
                      {species.charAt(0).toUpperCase() + species.slice(1)}
                    </option>
                  ))}
                </select>
              </div>

              {/* Breed Filter */}
              <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Breed</label>
                <select
                  value={filters.breed}
                  onChange={(e) => handleFilterChange('breed', e.target.value)}
                  className="select w-full"
                  disabled={!filters.species}
                >
                  <option value="">All Breeds</option>
                  {breedsList?.map((breed) => (
                    <option key={breed} value={breed}>
                      {breed}
                    </option>
                  ))}
                </select>
              </div>

              {/* Size Filter */}
              <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Size</label>
                <select
                  value={filters.size}
                  onChange={(e) => handleFilterChange('size', e.target.value)}
                  className="select w-full"
                >
                  <option value="">All Sizes</option>
                  <option value="small">Small</option>
                  <option value="medium">Medium</option>
                  <option value="large">Large</option>
                  <option value="extra_large">Extra Large</option>
                </select>
              </div>

              {/* Price Range */}
              <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Price Range</label>
                <div className="flex space-x-2">
                  <input
                    type="number"
                    placeholder="Min"
                    value={filters.minPrice}
                    onChange={(e) => handleFilterChange('minPrice', e.target.value)}
                    className="input w-full"
                  />
                  <input
                    type="number"
                    placeholder="Max"
                    value={filters.maxPrice}
                    onChange={(e) => handleFilterChange('maxPrice', e.target.value)}
                    className="input w-full"
                  />
                </div>
              </div>
            </div>
          </div>

          {/* Pets Grid */}
          <div className="lg:w-3/4">
            {/* Results Count */}
            <div className="mb-6">
              <p className="text-gray-600">
                {isLoading ? 'Loading...' : `Found ${petsData?.data?.length || 0} pets`}
              </p>
            </div>

            {isLoading ? (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {[...Array(12)].map((_, i) => (
                  <div key={i} className="bg-white rounded-lg shadow-md overflow-hidden animate-pulse">
                    <div className="bg-gray-300 h-48"></div>
                    <div className="p-4">
                      <div className="bg-gray-300 h-4 rounded mb-2"></div>
                      <div className="bg-gray-300 h-4 rounded w-3/4 mb-2"></div>
                      <div className="bg-gray-300 h-4 rounded w-1/2"></div>
                    </div>
                  </div>
                ))}
              </div>
            ) : petsData?.data?.length === 0 ? (
              <div className="text-center py-12">
                <PawPrint className="h-16 w-16 text-gray-400 mx-auto mb-4" />
                <h3 className="text-xl font-semibold text-gray-900 mb-2">No pets found</h3>
                <p className="text-gray-600 mb-4">Try adjusting your filters or search terms</p>
                <button
                  onClick={() => {
                    setFilters({
                      species: '',
                      breed: '',
                      size: '',
                      minPrice: '',
                      maxPrice: ''
                    })
                    setSearchQuery('')
                  }}
                  className="btn-primary"
                >
                  Clear Filters
                </button>
              </div>
            ) : (
              <>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                  {petsData?.data?.map((pet) => (
                    <div key={pet.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
                      <div className="relative">
                        <img
                          src={pet.images?.[0] || '/placeholder-pet.jpg'}
                          alt={pet.name}
                          className="w-full h-48 object-cover"
                        />
                        <button
                          onClick={() => handleAddToWishlist(pet.id)}
                          className="absolute top-2 right-2 p-2 bg-white rounded-full shadow-md hover:bg-gray-50 transition-colors"
                        >
                          <Heart className="h-4 w-4 text-gray-600" />
                        </button>
                      </div>
                      <div className="p-4">
                        <h3 className="text-lg font-semibold text-gray-900 mb-1">{pet.name}</h3>
                        <p className="text-sm text-gray-600 mb-2">
                          {pet.breed} • {pet.age} year{pet.age !== 1 ? 's' : ''} old
                        </p>
                        <p className="text-sm text-gray-600 mb-2 capitalize">{pet.size} • {pet.gender}</p>
                        <div className="flex items-center justify-between">
                          <p className="text-xl font-bold text-primary-500">${pet.price}</p>
                          <Link
                            to={`/pets/${pet.id}`}
                            className="bg-primary-500 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-primary-600 transition-colors"
                          >
                            View Details
                          </Link>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>

                {/* Pagination */}
                {totalPages > 1 && (
                  <div className="flex justify-center items-center space-x-2 mt-8">
                    <button
                      onClick={() => setCurrentPage(prev => Math.max(prev - 1, 1))}
                      disabled={currentPage === 1}
                      className="p-2 rounded-md border border-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
                    >
                      <ChevronLeft className="h-5 w-5" />
                    </button>
                    
                    {[...Array(totalPages)].map((_, i) => (
                      <button
                        key={i + 1}
                        onClick={() => setCurrentPage(i + 1)}
                        className={`px-3 py-2 rounded-md text-sm font-medium ${
                          currentPage === i + 1
                            ? 'bg-primary-500 text-white'
                            : 'border border-gray-300 hover:bg-gray-50'
                        }`}
                      >
                        {i + 1}
                      </button>
                    ))}
                    
                    <button
                      onClick={() => setCurrentPage(prev => Math.min(prev + 1, totalPages))}
                      disabled={currentPage === totalPages}
                      className="p-2 rounded-md border border-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
                    >
                      <ChevronRight className="h-5 w-5" />
                    </button>
                  </div>
                )}
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Pets