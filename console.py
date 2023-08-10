#!/usr/bin/python3
"""
HBNB Console Implementation
Contains the entry point of the command interpreter
"""

import cmd
import re
from shlex import split

from models.base_model import BaseModel
from models import storage



class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class represents the console
    """

    prompt = "(hbnb) "

    object_classes = {
        'BaseModel':BaseModel
    }

    def do_create(self, cls_name):
        if not cls_name:
            print("** class name missing **")
        elif cls_name not in self.object_classes.keys():
            print("** class doesn't exist **")
        else:
            Klass = self.object_classes[cls_name]
            new_instance = Klass()
            new_instance.save()

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
