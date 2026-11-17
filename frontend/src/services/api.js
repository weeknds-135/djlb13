const API = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api';
async function get(path) { const response = await fetch(`${API}${path}`); if (!response.ok) throw new Error(`La API respondió ${response.status}`); return response.json(); }
export const getProducts = () => get('/productos/');
export const getCategories = () => get('/categorias/');