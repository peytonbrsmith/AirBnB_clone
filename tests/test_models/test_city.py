#!/usr/bin/python3
"""City Model Unit tests"""


import unittest
import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test normal base instantiation"""
    def test_City(self):
        # Tests values after creating Base Model
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city.id, str)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()
