#!/usr/bin/python3
"""
HBNB Console Implementation
Contains the entry point of the command interpreter
"""

import cmd
import re
from shlex import split

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


def parse_arguments(arg):
    """Parses arguments from the input string"""
    curly_braces_match = re.search(r"\{(.*?)\}", arg)
    brackets_match = re.search(r"\[(.*?)\]", arg)

    if curly_braces_match is None:
        if brackets_match is None:
            # No special characters, split arguments using shlex
            arguments = split(arg)
        else:
            # Split arguments up to the first square bracket
            lexer = split(arg[: brackets_match.span()[0]])
            arguments = [i.strip(",") for i in lexer]
            arguments.append(brackets_match.group())
    else:
        # Split arguments up to the first curly brace
        lexer = split(arg[: curly_braces_match.span()[0]])
        arguments = [i.strip(",") for i in lexer]
        arguments.append(curly_braces_match.group())
    return arguments


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class represents the console
    """

    prompt = "(hbnb) "

    object_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }


    def default(self, line):
        """
        Called on an input line when the command prefix is not recognized
        """
        import re
        if re.search(r"\.", line) is None:
            print("*** Unknown syntax: {}".format(line))
            return False
        cls_name = re.split('\.', line)[0]
        extra_args = re.split("\(|\)", re.split('\.', line)[1])
        func = extra_args[0]
        args = re.split('\,', extra_args[1])
        str_args = " ".join(args)
        prompt = func + " " +  cls_name + " " +str_args
        HBNBCommand().onecmd(prompt)

    def do_create(self, cls_name):
        """
        Usage: create <class>
        Create command to create a new instance
        """
        cmd = parse_arguments(cls_name)
        if not cls_name:
            print("** class name missing **")
        elif cls_name not in self.object_classes.keys():
            print("** class doesn't exist **")
        else:
            _class = cmd[0]
            Klass = self.object_classes[_class]
            new_instance = Klass()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, cls_name):
        """
        Usage: show <class> <id>
        Prints the string representation of an instance
        based on the class name and id
        """
        cmd = parse_arguments(cls_name)
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.object_classes.keys():
            print("** class doesn't exist **")
        elif len(cmd) != 2:
            print("** instance id missing **")
        else:
            instance_repr = f"{cmd[0]}.{cmd[1]}"
            objects = storage.all()
            if instance_repr not in objects:
                print("** no instance found **")
            else:
                print(objects[instance_repr])

    def do_destroy(self, cls_name):
        """
        Usage: destroy <class> <id>
        Deletes an instance based on the class name and id
        """
        cmd = parse_arguments(cls_name)
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.object_classes.keys():
            print("** class doesn't exist **")
        elif len(cmd) != 2:
            print("** instance id missing **")
        else:
            instance_repr = f"{cmd[0]}.{cmd[1]}"
            objects = storage.all()
            if instance_repr not in objects:
                print("** no instance found **")
            else:
                del storage.all()[instance_repr]
                storage.save()

    def do_all(self, prompt):
        """
        Usage: all or all <class> or <class>.all()
        Prints all string representation of all
        instances based or not on the class name
        """
        args = parse_arguments(prompt)
        list_objects = []
        saved_objects = storage.all()
        if len(args) == 0:
            list_objects = [str(obj) for obj in saved_objects.values()]
        elif args[0] not in self.object_classes.keys():
            print("** class doesn't exist **")
        else:
            Klass = args[0]
            for obj in saved_objects.values():
                if type(obj).__name__ == Klass:
                    list_objects.append(str(obj))
        if len(list_objects) > 0:
            print(list_objects)

    def do_update(self, prompt):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = parse_arguments(prompt)
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in self.object_classes.keys():
            print("** class doesn't exist **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        elif f"{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
            return False
        elif len(args) == 2:
            print("** attribute name missing **")
            return False
        elif len(args) == 3:
            print("** value missing **")
            return False

        object_class, object_id = args[0], args[1]
        update_attr, attr_value = args[2], args[3]
        instance_repr = f"{args[0]}.{args[1]}"
        if len(args) == 4:
            setattr(objects[instance_repr], update_attr, attr_value)
        elif type(eval(update_attr)) == dict:
            for key, value in eval(update_attr).items():
                setattr(storage_objects[instance_repr], key, value)
        else:
            setattr(objects[instance_repr], update_attr, attr_value)
        objects[instance_repr].save()

    def do_count(self, prompt):
        """
        Usage: count <class> or <class>.count()
        Retrieves the number of instances of a class
        """
        count = 0
        args = parse_arguments(prompt)
        objects = storage.all()
        for key, value in objects.items():
            if key.split('.')[0] == args[0]:
                count += 1
        print(count)

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the prompt
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
