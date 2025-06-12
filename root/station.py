# ============================================================================
# FILE: station.py
# ============================================================================

class Station:
    """Represents a BART station with name and coordinates."""
    
    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
    def get_name(self) -> str:
        return self.name
    
    def get_latitude(self) -> float:
        return self.latitude
    
    def get_longitude(self) -> float:
        return self.longitude
    
    def __str__(self) -> str:
        return self.name
