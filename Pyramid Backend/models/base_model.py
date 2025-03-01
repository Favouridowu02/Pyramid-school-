#!/usr/bin/python3
"""
    This Module contains the base Model for the classes
"""
from sqlalchemy import Column, Integer, DateTime, Boolean, String
from sqlalchemy.orm import DeclarativeBase
from uuid import uuid4
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class Base(DeclarativeBase):
    """
        This class is used to Create the Base Class
    """
    pass


def generate_uuid():
    return str(uuid4())


class BaseModel:
    """
        This class Represents the base Model

        Methods:
            - to_dict: To convert the instance of this class to a Json format
            - save: To save the instance of the class to the Engine{Database}
            - delete: This is used to delete the object from the
                        Engine{Database}
            - update: This is used to update the object in the
                        Engine{Database}

        Attributes:
            - id: The uuid instance used to uniquely represent the object
            - created_at: This is used to represent when the object was created
            - updated_at: This is used to represent when the object
                            was last updated
    """
    id = Column(String(60), primary_key=True, default=generate_uuid)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """This method is used to return the json format of the Object"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict['updated_at'].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def __str__(self):
        """
            This Method is used to represent the String Representation
        """
        return "[{:s} ({}) {}]".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            This method is used to save the instance to the Engine Storage
        """
        from models import storage
        storage.new(self)
        storage.save()

    def delete(self):
        """
            This Method is used to delete an instance from the database Model
        """
        from models import storage
        storage.add(self)
        storage.save()