// API client for frontend/backend communication
import axios from 'axios';

// Get base URL from environment
const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

// Create axios instance
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add JWT token to requests
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle token expiration
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Clear token and redirect to login if token is expired
      localStorage.removeItem('access_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Authentication endpoints
export const authAPI = {
  register: (userData) => apiClient.post('/auth/register', userData),
  login: (credentials) => apiClient.post('/auth/login', credentials),
  logout: () => apiClient.post('/auth/logout'),
};

// User endpoints
export const userAPI = {
  getCurrentUser: () => apiClient.get('/users/me'),
};

// Task endpoints
export const taskAPI = {
  getTasks: (params) => apiClient.get('/tasks', { params }),
  createTask: (taskData) => apiClient.post('/tasks', taskData),
  getTask: (taskId) => apiClient.get(`/tasks/${taskId}`),
  updateTask: (taskId, taskData) => apiClient.put(`/tasks/${taskId}`, taskData),
  deleteTask: (taskId) => apiClient.delete(`/tasks/${taskId}`),
};

export default apiClient;