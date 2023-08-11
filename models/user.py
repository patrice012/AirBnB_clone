#!/usr/bin/python3
"""
Define User class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class use to define User

    Attributes:
        email(str): empty string
        password(str): empty string
        first_name(str): empty string
        last_name(str): empty string
    """
