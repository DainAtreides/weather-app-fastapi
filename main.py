from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.app_routes import router

# Create an instance of the FastAPI application
app = FastAPI()

# Mount the 'static' directory to serve static files (e.g., CSS, JavaScript, images)
app.mount('/static', StaticFiles(directory='static'), name='static')

# Include the router from app_routes to define the API routes
app.include_router(router)
