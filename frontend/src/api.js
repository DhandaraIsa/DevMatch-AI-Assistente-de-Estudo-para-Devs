import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Add token to requests
api.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authAPI = {
  register: (name, email, password) => 
    api.post('/auth/register', { name, email, password }),
  login: (email, password) => 
    api.post('/auth/login', { email, password })
};

export const aiAPI = {
  generatePlan: (topic, level) => 
    api.post('/ai/plan', { topic, level }),
  generateQuestions: (topic, level) => 
    api.post('/ai/questions', { topic, level }),
  generateExplanation: (topic, level, error_text) => 
    api.post('/ai/explain', { topic, level, error_text })
};

export const historyAPI = {
  getHistory: () => 
    api.get('/history')
};

export default api;
