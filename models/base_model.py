#!/usr/bin/python3
"""
BaseModel that defines all common attributes/methods for other classes
"""


from uuid import uuid4
from datetime import datetime

# from models import storage


class BaseModel:
    """
    BaseModel reprentation

    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        to_dict(self)
    """

    def __init__(self):
        """
        Init the new instance or object

        Attributes:
            id(str): uuid when an instance is created
            created_at(datetime): current datetime when an instance is created
            updated_at(datetime):  current datetime when an instance is created
                and it will be updated every time you change your object
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return the string representation of the instance

        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        _cls = self.__class__.__name__
        return "[{}] ({}) <{}>".format(_cls, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        _dict = {"__class__": self.__class__.__name__, **self.__dict__}
        _dict["created_at"] = _dict["created_at"].isoformat()
        _dict["updated_at"] = _dict["updated_at"].isoformat()
        return _dict
