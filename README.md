# AI Chatbot with Docker

A modern AI-powered chatbot built with React frontend and FastAPI backend, containerized with Docker for easy deployment.

## 🚀 Features

- **Frontend**: React + TypeScript + Tailwind CSS + shadcn/ui
- **Backend**: FastAPI + Python
- **AI Integration**: GROQ API for LLM responses
- **Containerization**: Docker + Docker Compose
- **Production Ready**: Nginx reverse proxy, health checks, and optimized builds

## 📋 Prerequisites

- [Docker](https://www.docker.com/get-started) and Docker Compose
- [GROQ API Key](https://console.groq.com/) (free account available)

## 🛠️ Quick Start

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Deploy_Project-sample
```

### 2. Set Up Environment Variables

**Option A: Using the setup script (Windows)**
```powershell
.\setup-env.ps1
```

**Option B: Manual setup**
```bash
# Create .env file
echo "GROQ_API_KEY=your_actual_groq_api_key_here" > .env
```

**Option C: Set environment variable directly**
```bash
# Windows PowerShell
$env:GROQ_API_KEY="your_actual_groq_api_key_here"

# Linux/Mac
export GROQ_API_KEY="your_actual_groq_api_key_here"
```

### 3. Get Your GROQ API Key
1. Visit [https://console.groq.com/](https://console.groq.com/)
2. Sign up for a free account
3. Create an API key
4. Replace `your_actual_groq_api_key_here` with your real API key

### 4. Build and Run
```bash
# Build and start all services
docker-compose up --build

# Or run in detached mode
docker-compose up -d --build
```

### 5. Access the Application
- **Frontend**: http://localhost
- **Backend API**: http://localhost:8004
- **Health Check**: http://localhost:8004/

## 🐳 Docker Commands

### Development
```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# View logs
docker-compose logs

# View specific service logs
docker-compose logs backend
docker-compose logs frontend
```

### Building
```bash
# Build all services
docker-compose build

# Build specific service
docker-compose build backend
docker-compose build frontend

# Rebuild without cache
docker-compose build --no-cache
```

### Management
```bash
# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Restart services
docker-compose restart

# Check service status
docker-compose ps
```

## 🏗️ Project Structure

```
├── backend/
│   ├── Dockerfile          # Backend container configuration
│   ├── main.py            # FastAPI application
│   ├── llm.py             # GROQ AI integration
│   └── requirements.txt   # Python dependencies
├── frontend/
│   ├── Dockerfile         # Frontend container configuration
│   ├── nginx.conf         # Nginx configuration
│   ├── src/               # React application source
│   └── package.json       # Node.js dependencies
├── docker-compose.yml     # Multi-container orchestration
├── setup-env.ps1         # Environment setup script (Windows)
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables
- `GROQ_API_KEY`: Your GROQ API key (required)
- `HOST`: Backend host (default: 0.0.0.0)
- `PORT`: Backend port (default: 8004)

### Ports
- **Frontend**: 80 (Nginx)
- **Backend**: 8004 (FastAPI)

## 🐛 Troubleshooting

### Common Issues

**Port 8004 already in use**
```bash
# Find and kill process using port 8004
netstat -ano | findstr :8004
taskkill /PID <process_id> /F
```

**GROQ API key not working**
- Verify your API key is correct
- Check if you have sufficient credits
- Ensure the key is properly set in environment variables

**Docker build fails**
```bash
# Clean Docker cache and rebuild
docker builder prune -f
docker-compose build --no-cache
```

**Frontend not loading**
- Check if nginx container is running: `docker-compose ps`
- View nginx logs: `docker-compose logs frontend`

### Health Checks
```bash
# Test backend health
curl http://localhost:8004/

# Test frontend
curl http://localhost/
```

## 🚀 Production Deployment

### Using Docker Compose
```bash
# Production deployment
docker-compose -f docker-compose.yml up -d --build
```

### Environment Security
- Never commit `.env` files to version control
- Use Docker secrets for production deployments
- Set up proper firewall rules
- Use HTTPS in production (configure SSL certificates)

## 📝 Development

### Local Development (without Docker)
```bash
# Backend
cd backend
pip install -r requirements.txt
python main.py

# Frontend
cd frontend
npm install
npm run dev
```

### Adding Dependencies
```bash
# Backend dependencies
# Edit backend/requirements.txt
docker-compose build backend

# Frontend dependencies
# Edit frontend/package.json
docker-compose build frontend
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. View the logs: `docker-compose logs`
3. Create an issue in the repository

---

**Happy Chatting! 🤖💬**
