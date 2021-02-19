#!/usr/bin/python3
"""Base Model Unit tests"""


import unittest
import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Test normal base instantiation"""
    def test_base(self):
        # Tests values after creating Base Model
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.id, str)

    def test_kwargs(self):
        """test base created with dictionary"""
        testdict = {"updated_at": "2021-02-18T23:26:48.287044",
                    "created_at": "2021-02-18T23:26:48.287044",
                    "id": "5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9",
                    "__class__": "BaseModel"}
        base2 = BaseModel(**testdict)
        self.assertIsInstance(base2, BaseModel)
        self.assertEqual(base2.id, "5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9")
        self.assertIsInstance(base2.updated_at, datetime.datetime)
        self.assertIsInstance(base2.created_at, datetime.datetime)
        self.assertIsInstance(base2.to_dict(), dict)

    def test_base_save(self):
        """test saving a base"""
        base3 = BaseModel()
        base3.save()
        self.assertNotEqual(base3.created_at, base3.updated_at)

if __name__ == '__main__':
    unittest.main()
