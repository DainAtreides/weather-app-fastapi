from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.app_routes import router


app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(router)

templates = Jinja2Templates(directory='static/templates')


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse('error.html', {
        'request': request,
        'error_code': exc.status_code,
        'error_message': exc.detail
    }, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return templates.TemplateResponse('error.html', {
        'request': request,
        'error_code': 400,
        'error_message': 'Validation error: ' + str(exc.errors())
    }, status_code=400)


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return templates.TemplateResponse('error.html', {
        'request': request,
        'error_code': 500,
        'error_message': f'An unexpected error occurred: {str(exc)}'
    }, status_code=500)
