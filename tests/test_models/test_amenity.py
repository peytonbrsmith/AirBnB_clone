#!/usr/bin/python3
"""Amenity Model Unit tests"""


import unittest
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test normal base instantiation"""
    def test_Amenity(self):
        # Tests values after creating Base Model
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity.id, str)
        self.assertEqual(Amenity.name, "")

if __name__ == '__main__':
    unittest.main()
