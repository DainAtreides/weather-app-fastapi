from fastapi import FastAPI
from routes.app_routes import router

app = FastAPI()
app.include_router(router)
