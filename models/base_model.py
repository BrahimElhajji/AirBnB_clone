#!/usr/bin/python3
"""
BaseModel file"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args
            **kwargs : Key/value pairs of attributes in dictionary.
        """
        datetimeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, datetimeform)
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
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """a dictionary containing all keys/values
        of __dict__ of the instance"""
        dic_inst = self.__dict__.copy()
        dic_inst["created_at"] = self.created_at.isoformat()
        dic_inst["updated_at"] = self.updated_at.isoformat()
        dic_inst["__class__"] = self.__class__.__name__
        return dic_inst
