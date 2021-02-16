#!/usr/bin/python3
"""Handles the User class"""

# Imports the Base Model Class
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User Class
    ========================
    Inherits from BaseModel.
    ========================

    Public Class Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string

    """
    # sets defaults to empty strings
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """Initializes with parent attributes"""
        super(User, self).__init__()
