#!/usr/bin/python3
import uuid
from datetime import datetime
import models
format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
  def __init__(self, *args, **kwargs):
    if kwargs:
      for key, value in kwargs.items():
        if key != "__class__":
          setattr(self, key, value)
      if hasattr(self, "created_at") and type(self.created_at) is str:
        self.created_at = datetime.strptime(kwargs["created_at"], format)
      if hasattr(self, "updated_at") and type(self.updated_at) is str:
        self.updated_at = datetime.strptime(kwargs["updated_at"], format)
    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
  
  def __str__(self):
    return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

  def save(self):
    self.updated_at = datetime.now()

  def to_dict(self):
    _dict = self.__dict__.copy()
    
    if "created_at" in _dict:
      _dict["created_at"] = self.created_at.isoformat()
    if "updated_at" in _dict:
      _dict["updated_at"] = self.updated_at.isoformat()
    _dict["__class__"] = self.__class__.__name__
    return _dict



