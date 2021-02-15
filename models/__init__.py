#!/usr/bin/python3
"""
This module initializes the Storage Engine
"""

from engine.file_storage import *

# Creates variable storage of class FileStorage
storage = FileStorage()
# Reads json data and loads it into the system
storage.reload()
