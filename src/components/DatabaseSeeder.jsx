import React, { useState } from 'react';
import axios from 'axios';

/**
 * Database Seeding Component
 * Triggers comprehensive data seeding (10 pets, 16 products in KES)
 * Only visible in development mode
 */
function DatabaseSeeder() {
    const [isLoading, setIsLoading] = useState(false);
    const [message, setMessage] = useState('');
    const [error, setError] = useState('');

    const seedDatabase = async () => {
        setIsLoading(true);
        setMessage('');
        setError('');

        try {
            const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';
            const response = await axios.post(`${apiUrl}/seed/init`);

            if (response.data.message.includes('already seeded')) {
                setMessage('📊 Database already has data. Clear it first if you want to reseed.');
            } else {
                setMessage(`✅ ${response.data.message}\n📊 Created ${response.data.pets} pets and ${response.data.products} products in ${response.data.currency}`);
            }
        } catch (err) {
            setError(`❌ Error: ${err.response?.data?.detail || err.message}`);
        } finally {
            setIsLoading(false);
        }
    };

    const clearDatabase = async () => {
        if (!window.confirm('Are you sure? This will DELETE ALL data!')) return;

        setIsLoading(true);
        setMessage('');
        setError('');

        try {
            const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';
            const response = await axios.post(`${apiUrl}/seed/clear`);
            setMessage(`✅ ${response.data.message}`);
        } catch (err) {
            setError(`❌ Error: ${err.response?.data?.detail || err.message}`);
        } finally {
            setIsLoading(false);
        }
    };

    // Only show in development
    if (import.meta.env.MODE !== 'development') {
        return null;
    }

    return (
        <div className="fixed bottom-4 right-4 z-50 bg-white p-6 rounded-lg shadow-lg border-2 border-gray-300 max-w-sm">
            <h3 className="font-bold text-lg mb-4">🛠️ Database Tools</h3>

            <div className="space-y-3">
                <button
                    onClick={seedDatabase}
                    disabled={isLoading}
                    className="w-full bg-green-500 hover:bg-green-600 disabled:bg-gray-400 text-white px-4 py-2 rounded font-semibold transition"
                >
                    {isLoading ? 'Seeding...' : '🌱 Seed Database'}
                </button>

                <button
                    onClick={clearDatabase}
                    disabled={isLoading}
                    className="w-full bg-red-500 hover:bg-red-600 disabled:bg-gray-400 text-white px-4 py-2 rounded font-semibold transition"
                >
                    {isLoading ? 'Processing...' : '🗑️ Clear Database'}
                </button>
            </div>

            {message && (
                <div className="mt-4 p-3 bg-green-100 border border-green-400 text-green-700 rounded whitespace-pre-wrap text-sm">
                    {message}
                </div>
            )}

            {error && (
                <div className="mt-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded whitespace-pre-wrap text-sm">
                    {error}
                </div>
            )}

            <p className="text-xs text-gray-500 mt-4">
                💡 Dev only. Seed: 10 pets + 16 products in KES
            </p>
        </div>
    );
}

export default DatabaseSeeder;
