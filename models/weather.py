from pydantic import BaseModel


class CurrentWeather(BaseModel):
    city_name: str
    temperature: float
    description: str
