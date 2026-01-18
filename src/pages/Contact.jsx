import React, { useState } from 'react'
import { useForm } from 'react-hook-form'
import { Mail, Phone, MapPin, Clock, Send } from 'lucide-react'
import toast from 'react-hot-toast'

function Contact() {
  const [isSubmitting, setIsSubmitting] = useState(false)

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors }
  } = useForm()

  const onSubmit = async (data) => {
    setIsSubmitting(true)
    // Simulate form submission
    await new Promise(resolve => setTimeout(resolve, 2000))
    console.log('Contact form submitted:', data)
    toast.success('Message sent successfully! We\'ll get back to you soon.')
    reset()
    setIsSubmitting(false)
  }

  const contactInfo = [
    {
      icon: Mail,
      title: 'Email Us',
      content: 'info@petbloom.com',
      description: 'We respond within 24 hours'
    },
    {
      icon: Phone,
      title: 'Call Us',
      content: '+254 716 115225',
      description: 'Mon-Fri 9AM-6PM EAT'
    },
    {
      icon: MapPin,
      title: 'Visit Us',
      content: 'Nairobi, Kenya',
      description: 'By appointment only'
    },
    {
      icon: Clock,
      title: 'Support Hours',
      content: '24/7 Online Support',
      description: 'Always here to help'
    }
  ]

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-primary-50 to-secondary-50 py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-4xl lg:text-5xl font-bold text-gray-900 mb-6">
              Contact <span className="text-primary-500">PetBloom</span>
            </h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Have questions about pet adoption or need support? We're here to help you every step of the way.
            </p>
          </div>
        </div>
      </section>

      {/* Contact Information */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {contactInfo.map((item, index) => (
              <div key={index} className="text-center p-6 bg-gray-50 rounded-lg">
                <div className="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                  <item.icon className="h-8 w-8 text-primary-500" />
                </div>
                <h3 className="text-lg font-semibold text-gray-900 mb-2">{item.title}</h3>
                <p className="text-gray-900 font-medium mb-1">{item.content}</p>
                <p className="text-sm text-gray-600">{item.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Form */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="bg-white rounded-lg shadow-lg overflow-hidden">
            <div className="bg-primary-500 px-6 py-8">
              <h2 className="text-2xl font-bold text-white text-center">Send Us a Message</h2>
              <p className="text-primary-100 text-center mt-2">
                We'd love to hear from you. Send us a message and we'll respond as soon as possible.
              </p>
            </div>

            <form onSubmit={handleSubmit(onSubmit)} className="p-8 space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    First Name
                  </label>
                  <input
                    type="text"
                    {...register('firstName', { required: 'First name is required' })}
                    className={`input ${errors.firstName ? 'border-red-500' : ''}`}
                    placeholder="John"
                  />
                  {errors.firstName && (
                    <p className="mt-1 text-sm text-red-600">{errors.firstName.message}</p>
                  )}
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Last Name
                  </label>
                  <input
                    type="text"
                    {...register('lastName', { required: 'Last name is required' })}
                    className={`input ${errors.lastName ? 'border-red-500' : ''}`}
                    placeholder="Doe"
                  />
                  {errors.lastName && (
                    <p className="mt-1 text-sm text-red-600">{errors.lastName.message}</p>
                  )}
                </div>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Email Address
                </label>
                <input
                  type="email"
                  {...register('email', {
                    required: 'Email is required',
                    pattern: {
                      value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                      message: 'Invalid email address'
                    }
                  })}
                  className={`input ${errors.email ? 'border-red-500' : ''}`}
                  placeholder="john@example.com"
                />
                {errors.email && (
                  <p className="mt-1 text-sm text-red-600">{errors.email.message}</p>
                )}
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Phone Number (Optional)
                </label>
                <input
                  type="tel"
                  {...register('phone')}
                  className="input"
                  placeholder="+254 716 115225"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Subject
                </label>
                <select
                  {...register('subject', { required: 'Please select a subject' })}
                  className={`select ${errors.subject ? 'border-red-500' : ''}`}
                >
                  <option value="">Select a subject</option>
                  <option value="adoption">Pet Adoption</option>
                  <option value="products">Product Inquiry</option>
                  <option value="breeding">Breeding Partnership</option>
                  <option value="support">Customer Support</option>
                  <option value="general">General Question</option>
                </select>
                {errors.subject && (
                  <p className="mt-1 text-sm text-red-600">{errors.subject.message}</p>
                )}
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Message
                </label>
                <textarea
                  {...register('message', { required: 'Message is required' })}
                  rows={6}
                  className={`textarea ${errors.message ? 'border-red-500' : ''}`}
                  placeholder="Tell us how we can help you..."
                />
                {errors.message && (
                  <p className="mt-1 text-sm text-red-600">{errors.message.message}</p>
                )}
              </div>

              <button
                type="submit"
                disabled={isSubmitting}
                className="w-full btn-primary flex items-center justify-center disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {isSubmitting ? (
                  <div className="flex items-center justify-center">
                    <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                    Sending...
                  </div>
                ) : (
                  <>
                    <Send className="mr-2 h-5 w-5" />
                    Send Message
                  </>
                )}
              </button>
            </form>
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section className="py-16 bg-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Frequently Asked Questions</h2>
            <p className="text-lg text-gray-600">
              Quick answers to common questions
            </p>
          </div>

          <div className="space-y-6">
            <div className="bg-gray-50 rounded-lg p-6">
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                How do I adopt a pet through PetBloom?
              </h3>
              <p className="text-gray-600">
                Browse our available pets, select your favorite, and complete the adoption process online.
                Our team will guide you through every step, including home verification and delivery arrangements.
              </p>
            </div>

            <div className="bg-gray-50 rounded-lg p-6">
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                Are your breeders verified?
              </h3>
              <p className="text-gray-600">
                Yes! All breeders on our platform go through a rigorous verification process, including
                facility inspections, health certifications, and background checks to ensure the highest standards.
              </p>
            </div>

            <div className="bg-gray-50 rounded-lg p-6">
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                What if I need help after adoption?
              </h3>
              <p className="text-gray-600">
                We provide ongoing support through our customer service team, veterinary partnerships,
                and educational resources. We're here to help ensure a smooth transition for both you and your new pet.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default Contact