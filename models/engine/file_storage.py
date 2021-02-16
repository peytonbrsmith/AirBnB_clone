#!/usr/bin/python3
"""
This is the File Storage Module

It handles the FileStorage class
"""


import json
from models.base_model import *
from models.state import *
from models.city import *
from models.user import *
from models.review import *
from models.place import *


class FileStorage():
    """
    the FileStorage class
    =====================

    Private class attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects by <class name>.id

    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects"""
        return(self.__objects)

    def new(self, obj):
        """
        Sets key/value pair in dictionary __objects

        Key Format: <obj class name>.<id>
            Ex: BaseModel.12121212
        """
        keystr = str(obj.__class__.__name__) + str(".") + obj.id
        self.__objects.update({keystr:obj.to_dict()})

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, mode='w+') as myFile:
            return myFile.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects"""
        with open(self.__file_path, mode='r') as myFile:
            self.__objects = json.loads(myFile.read())
            return
