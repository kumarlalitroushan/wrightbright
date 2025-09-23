#!/usr/bin/env bash
# Exit on any error
set -o errexit

echo "🚀 Starting build process..."

# Update pip to latest version
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo "📚 Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Collect static files for production
echo "🎨 Collecting static files..."
python manage.py collectstatic --no-input --clear

# Run database migrations
echo "🗄️  Running database migrations..."
python manage.py migrate

echo "✅ Build completed successfully!"
