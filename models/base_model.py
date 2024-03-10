#!/usr/bin/python3
"""
BaseModel

"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    a class BaseModel that defines
    all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instances of the BaseModel
        Args:
            @id:
            @created_at:
            @updated_at:
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.fromisoformat(v)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at with
        the current time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """a dictionary containing all keys/values
        of __dict__ of the instance"""
        dic_inst = self.__dict__.copy()
        dic_inst["created_at"] = self.created_at.isoformat()
        dic_inst["updated_at"] = self.updated_at.isoformat()
        dic_inst["__class__"] = self.__class__.__name__
        return dic_inst
