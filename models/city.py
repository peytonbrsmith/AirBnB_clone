#!/usr/bin/python3
"""Handles the City class"""


# Imports the Base Model Class
BaseModel = __import__('BaseModel').BaseModel


class City(BaseModel):
    """
    The City Class
    ========================
    Inherits from BaseModel.
    ========================

    Public Class Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    name = ""
    state_id = ""
