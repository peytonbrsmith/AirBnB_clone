#!/usr/bin/python3
"""State Model Unit tests"""


import unittest
import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test normal base instantiation"""
    def test_State(self):
        # Tests values after creating Base Model
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state.id, str)
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
