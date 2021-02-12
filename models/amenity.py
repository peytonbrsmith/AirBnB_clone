#!/usr/bin/python3
"""Handles the Amenity class"""


# Imports the Base Model Class
BaseModel = __import__('BaseModel').BaseModel


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
