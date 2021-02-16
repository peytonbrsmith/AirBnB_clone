#!/usr/bin/python3
"""Handles the Amenity class"""


# Imports the Base Model Class
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    The Amenity Class
    ========================
    Inherits from BaseModel.
    ========================

    Public Class Attributes:
        name: string - empty string

    """
    name = ""

    def __init__(self):
        """Initializes with parent attributes"""
        super(Amenity, self).__init__()
