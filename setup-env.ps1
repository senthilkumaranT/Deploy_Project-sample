# Setup Environment Variables for AI Chatbot
Write-Host "🔧 Setting up environment variables for AI Chatbot" -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan

# Check if .env file exists
if (Test-Path ".env") {
    Write-Host "✅ .env file already exists" -ForegroundColor Green
} else {
    Write-Host "📝 Creating .env file..." -ForegroundColor Yellow
    @"
# GROQ API Configuration
GROQ_API_KEY=your_groq_api_key_here

# Backend Configuration
HOST=0.0.0.0
PORT=8004

# Frontend Configuration
VITE_API_URL=http://localhost:8004
"@ | Out-File -FilePath ".env" -Encoding UTF8
    Write-Host "✅ .env file created" -ForegroundColor Green
}

Write-Host ""
Write-Host "🔑 IMPORTANT: You need to set your GROQ API key!" -ForegroundColor Red
Write-Host "1. Get your API key from: https://console.groq.com/" -ForegroundColor Yellow
Write-Host "2. Edit the .env file and replace 'your_groq_api_key_here' with your actual API key" -ForegroundColor Yellow
Write-Host "3. Or set it as an environment variable: `$env:GROQ_API_KEY='your_actual_key'" -ForegroundColor Yellow
Write-Host ""
Write-Host "🚀 After setting the API key, run: docker-compose up --build" -ForegroundColor Cyan
