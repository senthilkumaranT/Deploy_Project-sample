# Docker Build Test Script for AI Chatbot
Write-Host "🐳 Testing Docker Build for AI Chatbot" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host "⚠️  .env file not found. Creating from example..." -ForegroundColor Yellow
    Copy-Item "env.example" ".env"
    Write-Host "📝 Please edit .env and add your GROQ_API_KEY" -ForegroundColor Yellow
}

Write-Host "🔍 Checking Docker and Docker Compose..." -ForegroundColor Blue
try {
    docker --version | Out-Null
    docker-compose --version | Out-Null
    Write-Host "✅ Docker and Docker Compose are available" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker or Docker Compose is not installed" -ForegroundColor Red
    exit 1
}

Write-Host "🧹 Cleaning up previous builds..." -ForegroundColor Blue
docker-compose down --remove-orphans
docker system prune -f

Write-Host "🔨 Building backend..." -ForegroundColor Blue
docker-compose build backend

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Backend build successful" -ForegroundColor Green
} else {
    Write-Host "❌ Backend build failed" -ForegroundColor Red
    exit 1
}

Write-Host "🔨 Building frontend..." -ForegroundColor Blue
docker-compose build frontend

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Frontend build successful" -ForegroundColor Green
} else {
    Write-Host "❌ Frontend build failed" -ForegroundColor Red
    exit 1
}

Write-Host "🚀 Starting services..." -ForegroundColor Blue
docker-compose up -d

Write-Host "⏳ Waiting for services to be ready..." -ForegroundColor Blue
Start-Sleep -Seconds 10

Write-Host "🔍 Testing backend health..." -ForegroundColor Blue
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8004/" -UseBasicParsing
    if ($response.StatusCode -eq 200) {
        Write-Host "✅ Backend is healthy" -ForegroundColor Green
    } else {
        Write-Host "❌ Backend health check failed" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ Backend is not accessible" -ForegroundColor Red
}

Write-Host "🔍 Testing frontend..." -ForegroundColor Blue
try {
    $response = Invoke-WebRequest -Uri "http://localhost/" -UseBasicParsing
    if ($response.StatusCode -eq 200) {
        Write-Host "✅ Frontend is accessible" -ForegroundColor Green
    } else {
        Write-Host "❌ Frontend is not accessible" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ Frontend is not accessible" -ForegroundColor Red
}

Write-Host "📊 Service status:" -ForegroundColor Blue
docker-compose ps

Write-Host "🎉 Docker build test completed!" -ForegroundColor Green
Write-Host "🌐 Access your app at: http://localhost" -ForegroundColor Cyan
Write-Host "🔧 Backend API at: http://localhost:8004" -ForegroundColor Cyan
