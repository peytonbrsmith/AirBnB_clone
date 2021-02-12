#!/usr/bin/python3
"""Handles the Review class"""


# Imports the Base Model Class
from models.base_model import BaseModel


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

    def __init__(self):
        """Initializes with parent attributes"""
        super(Review, self).__init__()
