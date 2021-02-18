#!/usr/bin/python3
"""
This is the File Storage Module

It handles the FileStorage class
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    the FileStorage class
    =====================

    Private class attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - will store all objects by <class name>.id

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
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, mode='w+') as myFile:
            return myFile.write(json.dumps({key: value.to_dict() for key, value
                                in self.__objects.items()}))

    def reload(self):
        """deserializes the JSON file to __objects"""
        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        with open(self.__file_path, mode='r') as myFile:
            json_dict = json.load(myFile)
        for key, value in json_dict.items():
            key_class = classes.get(key.split('.')[0])
            self.__objects[key] = key_class(**value)
