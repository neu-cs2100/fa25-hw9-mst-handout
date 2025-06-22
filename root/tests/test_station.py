# FILE: test_station.py

#!/usr/bin/env python3
"""
Test file for station.py module.
Tests the Station class functionality.
"""

import unittest
from station import Station


class TestStation(unittest.TestCase):
    """Test cases for the Station class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # TODO: Create test Station objects with different names and coordinates
        # Example: self.station1 = Station("Downtown Berkeley", 37.8700, -122.2681)
        pass
    
    def test_init(self):
        """Test Station initialization."""
        # TODO: Create a Station object and verify that all attributes are set correctly
        # Test that name, latitude, and longitude are stored properly
        pass
    
    def test_get_name(self):
        """Test get_name method."""
        # TODO: Test that get_name() returns the correct station name
        pass
    
    def test_get_latitude(self):
        """Test get_latitude method."""
        # TODO: Test that get_latitude() returns the correct latitude
        pass
    
    def test_get_longitude(self):
        """Test get_longitude method."""
        # TODO: Test that get_longitude() returns the correct longitude
        pass
    
    def test_str_representation(self):
        """Test string representation of Station."""
        # TODO: Test that str(station) returns the station name
        pass
    
    def test_edge_cases(self):
        """Test edge cases for Station."""
        # TODO: Test stations with edge case coordinates (0, negative values, etc.)
        # TODO: Test stations with empty or special character names
        # TODO: Test stations with very long names
        pass


if __name__ == '__main__':
    unittest.main()
