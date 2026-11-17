# Lima Lectora

Catálogo inicial para una librería independiente. El frontend React consulta categorías y productos a una API Django REST Framework. La tienda muestra inventario de ejemplo y filtra por categoría; no procesa compras.

## Requisitos
Node.js 20.19+ o 22.12+, npm, Python 3.10+ y pip.

## Backend
```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_catalog
python manage.py runserver
```
API: `http://127.0.0.1:8000/api/productos/` y `/api/categorias/`. Admin: crea un usuario con `python manage.py createsuperuser`.

## Frontend
En otra terminal: `cd frontend`, `npm install`, `npm run dev`. Vite publica la interfaz en `http://localhost:5173`. La URL de API se cambia con `VITE_API_URL` en un archivo `.env`.

## Organización
`frontend/src/components` contiene piezas de interfaz; `services/api.js` concentra fetch; `backend/catalogo` contiene modelos, serializadores, vistas y rutas. Se usa SQLite local para facilitar el laboratorio.

## Rubro y alcance
Librería con narrativa, aprendizaje y literatura peruana. La primera versión permite explorar el catálogo, ver existencias y filtrar por categoría. El carrito, pedidos, autenticación y pagos quedan para siguientes iteraciones.

## GitHub
Para publicarlo: crea un repositorio vacío y ejecuta `git init`, `git add .`, `git commit -m "Implementa catálogo Lima Lectora"`, `git branch -M main` y `git remote add origin <URL>` seguido de `git push -u origin main`.
# djlb13
