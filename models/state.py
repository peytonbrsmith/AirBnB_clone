#!/usr/bin/python3
"""Handles the State class"""


# Imports the Base Model Class
BaseModel = __import__('BaseModel').BaseModel


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
