#!/bin/bash

echo "🐳 Testing Docker Build for AI Chatbot"
echo "======================================"

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Creating from example..."
    cp env.example .env
    echo "📝 Please edit .env and add your GROQ_API_KEY"
fi

echo "🔍 Checking Docker and Docker Compose..."
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed or not in PATH"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed or not in PATH"
    exit 1
fi

echo "✅ Docker and Docker Compose are available"

echo "🧹 Cleaning up previous builds..."
docker-compose down --remove-orphans
docker system prune -f

echo "🔨 Building backend..."
docker-compose build backend

if [ $? -eq 0 ]; then
    echo "✅ Backend build successful"
else
    echo "❌ Backend build failed"
    exit 1
fi

echo "🔨 Building frontend..."
docker-compose build frontend

if [ $? -eq 0 ]; then
    echo "✅ Frontend build successful"
else
    echo "❌ Frontend build failed"
    exit 1
fi

echo "🚀 Starting services..."
docker-compose up -d

echo "⏳ Waiting for services to be ready..."
sleep 10

echo "🔍 Testing backend health..."
curl -f http://localhost:8004/ > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Backend is healthy"
else
    echo "❌ Backend health check failed"
fi

echo "🔍 Testing frontend..."
curl -f http://localhost/ > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Frontend is accessible"
else
    echo "❌ Frontend is not accessible"
fi

echo "📊 Service status:"
docker-compose ps

echo "🎉 Docker build test completed!"
echo "🌐 Access your app at: http://localhost"
echo "🔧 Backend API at: http://localhost:8004"
