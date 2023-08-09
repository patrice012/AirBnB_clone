#!/usr/bin/python3
"""
HBNB Console Implementation
Contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class represents the console
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
