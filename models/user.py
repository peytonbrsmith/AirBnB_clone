#!/usr/bin/python3
"""Handles the User class"""

# Imports the Base Model Class
BaseModel = __import__('BaseModel').BaseModel


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
