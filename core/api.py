import requests
from config import API_KEY, BASE_URL


# Function to build the API request URL using the provided endpoint and city name
def build_url(endpoint: str, city_name: str) -> str:
    # Return the formatted URL string for the API request
    return f'{BASE_URL}/{endpoint}?q={city_name}&appid={API_KEY}&units=metric'


# Function to send a GET request and retrieve JSON data
def get_json(url: str) -> dict:
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Raise an exception if the request was unsuccessful
    response.raise_for_status()

    # Return the response data as a JSON dictionary
    return response.json()
