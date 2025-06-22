# FILE: station_map.py

import math
from typing import List
from graph import Graph
from station import Station


class StationMap:
    """Graph representation of BART stations built from CSV data."""
    
    # Constants
    STATION_DATA_FILE = "BART.csv" #Whatever the actual csv will be
    EARTH_RADIUS_IN_MILES = 3963
    NUM_STATIONS = -1  # When set to -1, all data is used;
    
    def __init__(self):
        self.graph: Graph[Station] = Graph()
        self._make_graph()
    
    def get_graph(self) -> Graph[Station]:
        """Get the graph representation of stations and distances between them."""
        return self.graph
    
    @staticmethod
    def _distance_in_miles(station1: Station, station2: Station) -> float:
        """
        Calculate the distance between two stations using the great circle formula.
        
        Formula: d = 3963.0 * arccos[(sin(lat1) * sin(lat2)) + cos(lat1) * cos(lat2) * cos(long2 – long1)]
        """
        lat1_rad = math.radians(station1.get_latitude())
        lat2_rad = math.radians(station2.get_latitude())
        lon1_rad = math.radians(station1.get_longitude())
        lon2_rad = math.radians(station2.get_longitude())
        
        return StationMap.EARTH_RADIUS_IN_MILES * math.acos(
            (math.sin(lat1_rad) * math.sin(lat2_rad)) +
            math.cos(lat1_rad) * math.cos(lat2_rad) * math.cos(lon2_rad - lon1_rad)
        )
    
    def _read_data_from_file(self) -> List[str]:
        """Read station data from CSV file."""
        try:
            with open(self.STATION_DATA_FILE, 'r', encoding='utf-8') as file:
                return file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"Unable to read file {self.STATION_DATA_FILE}")
    
    def _make_graph(self) -> None:
        """
        TODO: Complete this method to build the graph.
        
        Steps:
        1. Read data from the CSV file
        2. Parse each line to create Station objects and add them as nodes
        3. Add edges connecting each pair of nodes with weight as distance in miles
        4. Use the _distance_in_miles helper method
        5. Since edges are undirected, add only one edge between each pair
        6. Do not add edges between a node and itself
        
        CSV format: station_name,station_id,longitude,latitude
        """
      
        
        # TODO: Parse CSV data and create nodes
        
            
            # TODO: Parse the line (split by comma)
            # TODO: Create Station object with name, latitude, longitude
            # TODO: Add station as a node to the graph
            # TODO: Increment num_stations_added
    pass
        
        # TODO: Add edges between all pairs of nodes
        # TODO: Calculate distance between each pair of stations
        # TODO: Add edge with distance as weight (convert to int)
        # TODO: Use nested loops to connect each pair of nodes
        # TODO: Avoid connecting a node to itself
        # TODO: Since edges are undirected, only add one edge per pair
    pass