#!/usr/bin/python3
"""Handles the Review class"""


# Imports the Base Model Class
BaseModel = __import__('BaseModel').BaseModel


class Review(BaseModel):
    """
    The Review Class
    ========================
    Inherits from BaseModel.
    ========================

    Public Class Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string

    """
    place_id = ""
    user_id = ""
    text = ""
