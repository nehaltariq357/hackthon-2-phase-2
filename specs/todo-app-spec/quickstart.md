# Quickstart Guide: Todo App Development

**Feature**: Todo App Spec | **Date**: 2026-02-05

## Getting Started

This guide will help you set up the development environment for the Todo Full-Stack Web Application.

## Prerequisites

- Python 3.11+ installed
- Node.js 18+ installed
- PostgreSQL client tools (for local development)
- Git
- Docker (optional, for containerized development)

## Environment Setup

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your actual configuration values
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables:
```bash
cp .env.example .env.local
# Edit .env.local with your actual configuration values
```

## Database Configuration

### Local Development
1. Install PostgreSQL locally or use Docker:
```bash
docker run --name todo-postgres -e POSTGRES_DB=tododb -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres:15
```

2. Set the DATABASE_URL in your .env file:
```bash
DATABASE_URL=postgresql://postgres:password@localhost:5432/tododb
```

### Neon Configuration
1. Create a Neon account and project
2. Copy the connection string to your .env file:
```bash
DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
```

## Running the Application

### Backend Development Server
```bash
cd backend
# Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows
# Run the development server
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at http://localhost:8000

### Frontend Development Server
```bash
cd frontend
npm run dev
```

The frontend will be available at http://localhost:3000

## API Documentation

Once the backend is running, API documentation is available at:
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## Running Tests

### Backend Tests
```bash
cd backend
# Activate virtual environment
source venv/bin/activate
# Run tests
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Database Migrations

To run database migrations:
```bash
cd backend
# Activate virtual environment
source venv/bin/activate
# Run migrations
alembic upgrade head
```

To create a new migration:
```bash
cd backend
# Activate virtual environment
source venv/bin/activate
# Create migration
alembic revision --autogenerate -m "Migration description"
```

## Environment Variables

### Backend (.env)
- `DATABASE_URL`: Database connection string
- `JWT_SECRET_KEY`: Secret key for JWT token signing
- `JWT_ALGORITHM`: Algorithm for JWT encoding (default: HS256)
- `JWT_ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiry time in minutes

### Frontend (.env.local)
- `NEXT_PUBLIC_API_BASE_URL`: Base URL for API calls (e.g., http://localhost:8000/api)

## Development Commands

### Backend
- `uvicorn src.main:app --reload` - Run development server
- `pytest` - Run tests
- `pytest --cov=src` - Run tests with coverage
- `black .` - Format code with Black
- `flake8 .` - Lint code

### Frontend
- `npm run dev` - Run development server
- `npm run build` - Build for production
- `npm run start` - Run production build
- `npm test` - Run tests
- `npm run lint` - Lint code
- `npm run format` - Format code

## Project Structure

```
backend/
├── src/
│   ├── models/     # SQLModel database models
│   ├── services/   # Business logic
│   ├── api/        # API route definitions
│   └── auth/       # Authentication logic
├── alembic/        # Database migrations
├── tests/          # Backend tests
├── requirements.txt # Python dependencies
└── main.py         # Application entry point

frontend/
├── src/
│   ├── components/ # React components
│   ├── pages/      # Next.js pages
│   ├── services/   # API clients and utilities
│   └── hooks/      # Custom React hooks
├── public/         # Static assets
├── package.json    # Node.js dependencies
└── next.config.js  # Next.js configuration
```

## Common Issues

### Port Already in Use
If ports 8000 or 3000 are already in use:
- Change port in backend: `uvicorn src.main:app --port 8001`
- Change port in frontend: Update NEXT_PUBLIC_API_BASE_URL accordingly

### Database Connection Issues
- Verify PostgreSQL is running
- Check DATABASE_URL in .env file
- Ensure firewall rules allow connections

### JWT Secret Issues
- Generate a strong secret for JWT_SECRET_KEY
- Use `openssl rand -hex 32` to generate a random hex string

## Next Steps

1. Start with the backend: Implement the User and Task models
2. Create the authentication endpoints
3. Implement the task management endpoints
4. Start the frontend: Create the login/register forms
5. Connect frontend to backend API
6. Implement task listing and management UI