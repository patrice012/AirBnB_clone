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
        _id = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[_id] = obj

    def save(self):
        """
        Save objects to file
        Usage:
            Serializes __objects to the JSON file (path: __file_path)
        """
        path = FileStorage.__file_path
        obj = FileStorage.__objects.items()
        with open(path, "w") as file:
            dict_objects = {key: value.to_dict() for key, value in obj}
            json.dump(dict_objects, file)

    @staticmethod
    def object_classes():
        """
        Helper function
        map class names to python class
        """
        from ..base_model import BaseModel

        classes = {"BaseModel": BaseModel}

        return classes

    @staticmethod
    def get_object_class(string_cls):
        """
        Select object class base on `string_cls`
        Args:
            string_cls(str): string name of the instance class
        Return:
            Instance's Class
        """
        if type(string_cls) is not str or string_cls is None:
            raise TypeError(f"{string_cls} must be a string object")
        classes = FileStorage.object_classes()
        return classes[string_cls]

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
                for key, value in storage_dict.items():
                    Klass = self.get_object_class(value.get("__class__", None))
                    storage_dict[key] = Klass(**value)
                FileStorage.__objects = storage_dict
