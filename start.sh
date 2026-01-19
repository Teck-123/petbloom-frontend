#!/bin/sh
set -e

# Set default backend URL if not provided
BACKEND_URL=${BACKEND_URL:-http://localhost:8000}

echo "Using backend URL: $BACKEND_URL"

# Substitute environment variables in nginx config
envsubst '\$BACKEND_URL' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

# Start nginx
exec nginx -g "daemon off;"
