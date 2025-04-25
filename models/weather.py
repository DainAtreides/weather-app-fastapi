from pydantic import BaseModel


# Define the CurrentWeather model to represent the weather data
class CurrentWeather(BaseModel):
    city_name: str
    temperature: float
    description: str
