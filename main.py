from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.app_routes import router


app = FastAPI()

# Mount the 'static' directory to serve static files (e.g., CSS, images)
app.mount('/static', StaticFiles(directory='static'), name='static')

# Include the router from app_routes to define the API routes
app.include_router(router)

templates = Jinja2Templates(directory='static/templates')


# Global exception handler for HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    # Render the error page with the error code and message
    return templates.TemplateResponse('error.html', {
        'request': request,
        'error_code': exc.status_code,
        'error_message': exc.detail
    }, status_code=exc.status_code)


# Global exception handler for RequestValidationError
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Render the error page for validation error with details
    return templates.TemplateResponse('error.html', {
        'request': request,
        'error_code': 400,
        'error_message': 'Validation error: ' + str(exc.errors())
    }, status_code=400)


# Global exception handler for all unexpected exceptions
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    # Render the error page for unexpected errors
    return templates.TemplateResponse('error.html', {
        'request': request,
        'error_code': 500,
        'error_message': f'An unexpected error occurred: {str(exc)}'
    }, status_code=500)
