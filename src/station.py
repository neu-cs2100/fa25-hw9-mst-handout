# FILE: station.py

class Station:
    """Represents a BART station with name and coordinates."""
    
    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
    def __str__(self) -> str:
        return self.name
