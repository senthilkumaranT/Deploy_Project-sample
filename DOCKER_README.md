# Docker Setup for AI Chatbot

This project is now containerized with Docker for easy deployment and development.

## 🐳 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- GROQ API key

### 1. Environment Setup
```bash
# Copy the example environment file
cp env.example .env

# Edit .env and add your GROQ API key
GROQ_API_KEY=your_actual_groq_api_key_here
```

### 2. Build and Run
```bash
# Build and start all services
docker-compose up --build

# Or run in detached mode
docker-compose up -d --build
```

### 3. Access the Application
- **Frontend**: http://localhost
- **Backend API**: http://localhost:8004
- **Health Check**: http://localhost:8004/

## 🛠️ Development Commands

### Build individual services
```bash
# Build backend only
docker-compose build backend

# Build frontend only
docker-compose build frontend
```

### Run specific services
```bash
# Run only backend
docker-compose up backend

# Run only frontend
docker-compose up frontend
```

### View logs
```bash
# All services
docker-compose logs

# Specific service
docker-compose logs backend
docker-compose logs frontend

# Follow logs
docker-compose logs -f backend
```

### Stop services
```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## 🔧 Configuration

### Environment Variables
- `GROQ_API_KEY`: Your GROQ API key (required)
- `HOST`: Backend host (default: 0.0.0.0)
- `PORT`: Backend port (default: 8004)

### Ports
- **Frontend**: 80 (nginx)
- **Backend**: 8004 (FastAPI)

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │
│   (Nginx)       │◄───┤   (FastAPI)     │
│   Port: 80      │    │   Port: 8004    │
└─────────────────┘    └─────────────────┘
```

## 🚀 Production Deployment

### Using Docker Compose
```bash
# Production build
docker-compose -f docker-compose.yml up -d --build

# Scale services (if needed)
docker-compose up -d --scale backend=2
```

### Using Docker Swarm
```bash
# Initialize swarm
docker swarm init

# Deploy stack
docker stack deploy -c docker-compose.yml ai-chatbot
```

## 🐛 Troubleshooting

### Check service status
```bash
docker-compose ps
```

### Check service health
```bash
# Backend health
curl http://localhost:8004/

# Frontend health
curl http://localhost/
```

### View detailed logs
```bash
docker-compose logs --tail=100 backend
```

### Rebuild after code changes
```bash
docker-compose up --build --force-recreate
```

## 📁 Project Structure
```
├── backend/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── main.py
│   ├── llm.py
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── nginx.conf
│   └── src/
├── docker-compose.yml
├── .dockerignore
└── env.example
```

## 🔒 Security Notes

- The application runs as non-root user in containers
- Nginx includes security headers
- Environment variables are properly isolated
- Health checks ensure service availability

## 📝 Development vs Production

### Development
- Hot reload disabled for stability
- All services in single compose file
- Basic nginx configuration

### Production
- Use production-ready nginx config
- Consider using Docker secrets for API keys
- Set up proper logging and monitoring
- Use reverse proxy (Traefik/Nginx) for SSL termination
