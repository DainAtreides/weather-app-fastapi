import requests
from config import API_KEY, BASE_URL


def build_url(endpoint: str, city_name: str) -> str:
    return f'{BASE_URL}/{endpoint}?q={city_name}&appid={API_KEY}&units=metric'


def get_json(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
