import requests
from geopy.geocoders import Nominatim
from config import API_KEY, BASE_URL
from fastapi.exceptions import HTTPException


# Function to build the URL for the weather API request
def build_url(endpoint: str, city_name: str) -> str:
    return f'{BASE_URL}/{endpoint}?q={city_name.strip()}&appid={API_KEY}&units=metric'


# Function to send an HTTP request and handle possible errors
def get_json(url: str) -> dict:
    city_name = url.split('q=')[1].split(
        '&')[0]  # Extract city name from the URL
    try:
        response = requests.get(url)  # Send the request
        response.raise_for_status()  # Check for HTTP errors
        return response.json()  # Return the JSON data if the request is successful
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            # Handle 404 errors (City not found)
            raise HTTPException(
                status_code=404, detail=f'{city_name} not found.')
        # Handle other HTTP errors
        raise HTTPException(
            status_code=500, detail='Failed to retrieve weather data.')
    except requests.exceptions.RequestException as e:
        # Handle request-related errors (e.g., network issues)
        raise HTTPException(status_code=500, detail=f'Request error: {str(e)}')


# Function to perform reverse geocoding and get the city name from latitude and longitude
def reverse_geocode(lat: float, lon: float) -> str:
    geolocator = Nominatim(user_agent='weather_app')  # Initialize geolocator
    location = geolocator.reverse(
        (lat, lon), language='en')  # Get location details
    if location and 'city' in location.raw['address']:
        return location.raw['address']['city']  # Return city if found
    elif location and 'town' in location.raw['address']:
        return location.raw['address']['town']  # Return town if found
    elif location and 'village' in location.raw['address']:
        return location.raw['address']['village']  # Return village if found
    else:
        return 'Unknown'  # Return 'Unknown' if no city, town, or village is found
