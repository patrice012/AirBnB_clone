#!/usr/bin/python3
"""
Module contains `FileStorage` class
"""
import json
import os


class FileStorage:
    """
    File Storage Class Representation
    Usage:
        Serializes instances to a JSON file
        Deserializes JSON file to instances

    WorkFlow:
        <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -
        JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -
        JSON load -> <class 'dict'> -> <class 'BaseModel'>

    Methodes:
        all: Returns the object
        new: updates the dictionary id
        save: Serializes, or converts Python objects into JSON strings
        reload: Deserializes, or converts JSON strings into Python objects.

    Attributes:
        __file_path(str): The name of the file to save objects to.
                string - path to the JSON file (ex: file.json)
        __objects(dict): A dictionary of instantiated objects.
                empty but will store all objects by <class name>.id
    """

    __file_path = "storage_file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Add new object to file storage
        Usage:
            Sets in __objects the obj with key <obj class name>.id
        """
        _id = f"{obj.__class__.__name__}.{obj.id}"
        setattr(FileStorage.__objects, _id, obj)

    def save(self):
        """
        Save objects to file
        Usage:
            Serializes __objects to the JSON file (path: __file_path)
        """
        path = FileStorage.__file_path
        obj = FileStorage.__objects.items()
        dict_objects = {key: value.to_dict() for key, value in obj}
        with open(path, "w") as file:
            json.dump(dict_objects, file)

    def reload(self):
        """
        Reload objects from file
        Usage:
            deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists
             If the file doesn’t exist, no exception should be raised)
        """
        path = FileStorage.__file_path
        if os.path.isfile(path):
            with open(path, "r") as file:
                storage_dict = json.load(file)
                storage_dict = {
                    k: self.classes()[v["__class__"]](**v)
                    for k, v in storage_dict.items()
                }
                FileStorage.__objects = storage_dict
