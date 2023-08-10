#!/usr/bin/python3
"""Defines unittest cases for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """Tests for prompting of the HBNB console."""

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", console.getvalue().strip())

    # @patch("sys.stdout", new_callable=StringIO)
    # def test_hello_output(self, mock_stdout):
    #     HBNBCommand().onecmd("help")
    #     expected_output = ""
    #     self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


class TestHBNBCommand_help(unittest.TestCase):
    """Tests for help messages of the HBNB console."""

    def test_help_quit(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help quit"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_help(self, mock_stdout):
        self.assertFalse(HBNBCommand().onecmd("help"))
        output = "Documented commands (type help <topic>):"
        self.assertIn(output, mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
