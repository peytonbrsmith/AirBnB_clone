#!/usr/bin/python3
"""File Storage Testing"""


import unittest
import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test normal base instantiation"""
    def test_file_storage(self):
        # Tests values after creating Base Model
        fs = FileStorage()
        base4 = BaseModel()
        fs.new(base4)
        self.assertIsInstance(fs, FileStorage)
        self.assertIsInstance(fs.all(), dict)
        self.assertIn("{}.{}".format("BaseModel", base4.id), fs.all())

if __name__ == '__main__':
    unittest.main()
