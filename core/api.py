import requests
from geopy.geocoders import Nominatim
from config import API_KEY, BASE_URL
from fastapi.exceptions import HTTPException


def build_url(endpoint: str, city_name: str) -> str:
    return f'{BASE_URL}/{endpoint}?q={city_name.strip()}&appid={API_KEY}&units=metric'


def get_json(url: str) -> dict:
    city_name = url.split('q=')[1].split('&')[0]
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=404, detail=f'{city_name} not found.')
        raise HTTPException(
            status_code=500, detail='Failed to retrieve weather data.')
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f'Request error: {str(e)}')


def reverse_geocode(lat: float, lon: float) -> str:
    geolocator = Nominatim(user_agent='weather_app')
    location = geolocator.reverse((lat, lon), language='en')
    if location and 'city' in location.raw['address']:
        return location.raw['address']['city']
    elif location and 'town' in location.raw['address']:
        return location.raw['address']['town']
    elif location and 'village' in location.raw['address']:
        return location.raw['address']['village']
    else:
        return 'Unknown'
