from abc import ABC, abstractmethod
from models.city import City


class Weather(ABC):
    def __init__(self, city: City):
        self.city = city
        self.temp = None
        self.description = None

    @abstractmethod
    def fetch(self):
        pass
