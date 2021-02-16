#!/usr/bin/python3
"""Handles the State class"""


# Imports the Base Model Class
from models.base_model import BaseModel


class State(BaseModel):
    """
    The State Class
    ========================
    Inherits from BaseModel.
    ========================

    Public Class Attributes:
        name: string - empty string

    """
    name = ""

    def __init__(self):
        """Initializes with parent attributes"""
        super(State, self).__init__()
