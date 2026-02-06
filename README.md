# Todo Full-Stack Web Application

This is a complete full-stack todo application built with a FastAPI backend and Next.js frontend, featuring JWT-based authentication and secure data isolation.

## Architecture

- **Backend**: FastAPI with SQLModel, PostgreSQL database
- **Frontend**: Next.js with React
- **Authentication**: JWT-based with secure token handling
- **Database**: PostgreSQL with Neon (production) or local SQLite (development)

## Features

- User registration and authentication
- Secure JWT-based session management
- Full CRUD operations for tasks
- User data isolation (users can only access their own tasks)
- Responsive UI that works on mobile and desktop
- Task filtering, search, and prioritization

## Project Structure

```
backend/                 # FastAPI backend
├── src/
│   ├── models/         # SQLModel database models
│   ├── services/       # Business logic
│   ├── api/            # API route definitions
│   ├── auth/           # Authentication logic
│   └── utils/          # Utilities and exceptions
├── alembic/            # Database migrations
├── requirements.txt    # Python dependencies
└── main.py             # Application entry point

frontend/               # Next.js frontend
├── pages/              # Next.js pages
├── src/
│   ├── components/     # React components
│   ├── services/       # API clients and utilities
│   └── styles/         # CSS styles
├── package.json        # Node.js dependencies
└── next.config.js      # Next.js configuration
```

## Setup Instructions

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

6. Run the development server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
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

4. Run the development server:
```bash
npm run dev
```

## Environment Variables

### Backend (.env)
- `DATABASE_URL`: Database connection string
- `JWT_SECRET_KEY`: Secret key for JWT token signing
- `JWT_ALGORITHM`: Algorithm for JWT encoding (default: HS256)
- `JWT_ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiry time in minutes

### Frontend (.env.local)
- `NEXT_PUBLIC_API_BASE_URL`: Base URL for API calls (e.g., http://localhost:8000)

## API Documentation

Once the backend is running, API documentation is available at:
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## Security Features

- JWT-based authentication with secure token handling
- User data isolation (each user can only access their own tasks)
- Password hashing using bcrypt
- Input validation and sanitization
- CORS configuration (should be restricted in production)

## Deployment

The application is designed for cloud deployment:
- Backend: Deploy as containerized service or serverless function
- Frontend: Deploy to static hosting (Vercel, Netlify, S3/CloudFront)
- Database: Use managed PostgreSQL service (Neon, AWS RDS, etc.)

## Technologies Used

- **Backend**: Python, FastAPI, SQLModel, PostgreSQL
- **Frontend**: JavaScript, Next.js, React, Axios
- **Authentication**: JWT, bcrypt
- **Database**: PostgreSQL (with Neon as provider)
- **Tools**: Uvicorn (ASGI server), Alembic (migrations)