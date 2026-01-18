import React from 'react'
import { Heart, Shield, Truck, Users, Star, PawPrint } from 'lucide-react'

function About() {
  const values = [
    {
      icon: Heart,
      title: 'Pet-First Philosophy',
      description: 'Every decision we make is guided by what\'s best for pets and their wellbeing.'
    },
    {
      icon: Shield,
      title: 'Trust & Safety',
      description: 'We thoroughly vet all breeders and ensure every pet is healthy and cared for.'
    },
    {
      icon: Users,
      title: 'Community Focused',
      description: 'Building a community of responsible pet owners and ethical breeders.'
    },
    {
      icon: Truck,
      title: 'Reliable Service',
      description: 'From adoption to delivery, we provide dependable support every step of the way.'
    }
  ]

  const stats = [
    { number: '1000+', label: 'Happy Pets Adopted' },
    { number: '500+', label: 'Verified Breeders' },
    { number: '98%', label: 'Customer Satisfaction' },
    { number: '24/7', label: 'Customer Support' }
  ]

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-primary-50 to-secondary-50 py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-4xl lg:text-5xl font-bold text-gray-900 mb-6">
              About <span className="text-primary-500">PetBloom</span>
            </h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              We're passionate about connecting loving families with healthy pets from verified breeders and shelters,
              while providing everything needed for a happy pet life.
            </p>
          </div>
        </div>
      </section>

      {/* Mission Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6">Our Mission</h2>
              <p className="text-lg text-gray-600 mb-6">
                PetBloom was founded with a simple yet powerful mission: to make pet adoption and care
                accessible, safe, and joyful for everyone involved. We believe every pet deserves a loving
                home, and every family deserves a healthy, happy companion.
              </p>
              <p className="text-lg text-gray-600 mb-6">
                By combining technology with compassion, we've created a platform that brings together
                responsible breeders, caring shelters, and loving families in a seamless, trustworthy
                ecosystem.
              </p>
              <p className="text-lg text-gray-600">
                Our commitment extends beyond adoption – we're here to support you throughout your
                entire pet parenthood journey with expert advice, premium supplies, and ongoing care.
              </p>
            </div>
            <div className="bg-primary-100 rounded-2xl p-8">
              <div className="grid grid-cols-2 gap-6">
                {stats.map((stat, index) => (
                  <div key={index} className="text-center">
                    <div className="text-3xl font-bold text-primary-600 mb-2">{stat.number}</div>
                    <div className="text-gray-700 font-medium">{stat.label}</div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Values Section */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Our Values</h2>
            <p className="text-lg text-gray-600">
              The principles that guide everything we do at PetBloom
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {values.map((value, index) => (
              <div key={index} className="bg-white rounded-lg shadow-md p-6 text-center">
                <div className="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                  <value.icon className="h-8 w-8 text-primary-500" />
                </div>
                <h3 className="text-lg font-semibold text-gray-900 mb-2">{value.title}</h3>
                <p className="text-gray-600">{value.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Team Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Meet Our Team</h2>
            <p className="text-lg text-gray-600">
              The passionate pet lovers behind PetBloom
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="bg-primary-100 w-32 h-32 rounded-full flex items-center justify-center mx-auto mb-4">
                <User className="h-16 w-16 text-primary-500" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Thecla Owano</h3>
              <p className="text-primary-500 font-medium mb-2">Co-Founder</p>
              <p className="text-gray-600">
                Passionate about pet welfare and connecting pets with loving families
              </p>
            </div>

            <div className="text-center">
              <div className="bg-secondary-100 w-32 h-32 rounded-full flex items-center justify-center mx-auto mb-4">
                <User className="h-16 w-16 text-secondary-500" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Alex Mureti</h3>
              <p className="text-secondary-500 font-medium mb-2">Co-Founder & Operations Lead</p>
              <p className="text-gray-600">
                Dedicated to ensuring the highest standards of pet care and welfare
              </p>
            </div>

            <div className="text-center">
              <div className="bg-accent-100 w-32 h-32 rounded-full flex items-center justify-center mx-auto mb-4">
                <User className="h-16 w-16 text-accent-500" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Sharon Soyian</h3>
              <p className="text-accent-500 font-medium mb-2">Customer Experience Lead</p>
              <p className="text-gray-600">
                Committed to making every pet adoption journey smooth and joyful
              </p>
            </div>

            <div className="text-center">
              <div className="bg-primary-100 w-32 h-32 rounded-full flex items-center justify-center mx-auto mb-4">
                <User className="h-16 w-16 text-primary-500" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">David Kamau</h3>
              <p className="text-primary-500 font-medium mb-2">Technology Lead</p>
              <p className="text-gray-600">
                Building innovative solutions to make pet adoption seamless and secure
              </p>
            </div>

            <div className="text-center">
              <div className="bg-secondary-100 w-32 h-32 rounded-full flex items-center justify-center mx-auto mb-4">
                <User className="h-16 w-16 text-secondary-500" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Vanessa Omondi</h3>
              <p className="text-secondary-500 font-medium mb-2">Marketing & Partnerships</p>
              <p className="text-gray-600">
                Growing our community and connecting pet lovers with quality products and services
              </p>
            </div>

            <div className="text-center">
              <div className="bg-accent-100 w-32 h-32 rounded-full flex items-center justify-center mx-auto mb-4">
                <User className="h-16 w-16 text-accent-500" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Ian Nasoore</h3>
              <p className="text-accent-500 font-medium mb-2">Breeder Relations Manager</p>
              <p className="text-gray-600">
                Ensuring our network of breeders meets the highest standards of ethical care
              </p>
            </div>
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
            Join thousands of families who have found their perfect pet through PetBloom
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a
              href="/pets"
              className="bg-white text-primary-500 px-8 py-3 rounded-lg font-medium hover:bg-gray-100 transition-colors"
            >
              Browse Available Pets
            </a>
            <a
              href="/contact"
              className="border-2 border-white text-white px-8 py-3 rounded-lg font-medium hover:bg-white hover:text-primary-500 transition-colors"
            >
              Contact Us
            </a>
          </div>
        </div>
      </section>
    </div>
  )
}

const User = ({ className }) => (
  <svg className={className} fill="currentColor" viewBox="0 0 20 20">
    <path fillRule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clipRule="evenodd" />
  </svg>
)

export default About