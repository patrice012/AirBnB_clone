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

from io import StringIO
from unittest.mock import patch

from models import storage
from models.engine.file_storage import FileStorage
from tests.helper import remove_file, DEBUG
from console import HBNBCommand


def setUpModule():
    """Change json file for testing to avoid side effect"""
    FileStorage._FileStorage__file_path = "test_console.json"


def tearDownModule():
    """Change json file to the default"""
    file = FileStorage._FileStorage__file_path
    if DEBUG:
        remove_file(file)
    FileStorage._FileStorage__file_path = "storage_file.json"


class TestHBNBCommand_prompting(unittest.TestCase):
    """Tests for prompting of the HBNB console."""

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", console.getvalue().strip())

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


class TestHBNBCommand_create(unittest.TestCase):
    """Tests for create command of the HBNB console."""

    @classmethod
    def setUpClass(cls):
        FileStorage.__objects = {}

    def test_create_object_using_BaseModel_class(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "BaseModel.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

    def test_create_object_using_Review_class(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "Review.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

    def test_create_object_using_User_class(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "User.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

    def test_create_object_using_Place_class(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "Place.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

    def test_create_object_using_State_class(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "State.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

    def test_create_object_using_Amenity_class(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "Amenity.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

    def test_create_object_using_City_class(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(console.getvalue().strip()))
            test_k = "City.{}".format(console.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())

    def test_create_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_create_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_create_invalid_syntax(self):
        expected = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(expected, console.getvalue().strip())

        expected = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(expected, console.getvalue().strip())


class TestHBNBCommand_show(unittest.TestCase):
    """Tests for show command of the HBNB console"""

    def test_show_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_show_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_show_missing_id_space_notation(self):
        expected = "** instance id missing **"
        models_list = [
            "show BaseModel",
            "show State",
            "show User" "show Amenity",
            "show City",
            "show Review",
            "show Place",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    self.assertEqual(expected, console.getvalue().strip())

    def test_show_no_instance_found_space_notation(self):
        expected = "** no instance found **"
        models_list = [
            "show BaseModel 1",
            "show State 1",
            "show User 1" "show Amenity 1",
            "show City 1",
            "show Review 1",
            "show Place 1",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    self.assertEqual(expected, console.getvalue().strip())

    def test_show_objects_space_notation(self):
        models_list = [
            "create BaseModel",
            "create State",
            "create User" "create Amenity",
            "create City",
            "create Review",
            "create Place",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    o_id = console.getvalue().strip()
                model = prompt.split()[1]
                with patch("sys.stdout", new=StringIO()) as console:
                    o = storage.all()["{}.{}".format(model, o_id)]
                    command = "show {} {}".format(model, o_id)
                    self.assertFalse(HBNBCommand().onecmd(command))
                    self.assertEqual(o.__str__(), console.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Tests for destroy command of the HBNB console."""

    @patch("sys.stdout", new_callable=StringIO)
    def setUp(self, mock_stdout):
        """Create all models instances for testing"""
        models_list = [
            "create BaseModel",
            "create State",
            "create User" "create Amenity",
            "create City",
            "create Review",
            "create Place",
        ]
        model = models_list[0]
        HBNBCommand().onecmd(model)

    def test_destroy_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_invalid_class(self):
        expected = "** class doesn't exist **"

        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_id_missing_space_notation(self):
        expected = "** instance id missing **"
        models_list = [
            "destroy BaseModel",
            "destroy State",
            "destroy User" "destroy Amenity",
            "destroy City",
            "destroy Review",
            "destroy Place",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_invalid_id_space_notation(self):
        expected = "** no instance found **"
        models_list = [
            "destroy BaseModel 1",
            "destroy State 1",
            "destroy User 1" "destroy Amenity 1",
            "destroy City 1",
            "destroy Review 1",
            "destroy Place 1",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_objects_space_notation(self):
        models_list = [
            "create BaseModel",
            "create State",
            "create User" "create Amenity",
            "create City",
            "create Review",
            "create Place",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    o_id = console.getvalue().strip()
                model = prompt.split()[1]

                with patch("sys.stdout", new=StringIO()) as console:
                    o = storage.all()["{}.{}".format(model, o_id)]
                    command = "show {} {}".format(model, o_id)
                    self.assertFalse(HBNBCommand().onecmd(command))
                    self.assertNotIn(o, storage.all())


class TestHBNBCommand_all(unittest.TestCase):
    """Tests for all command of the HBNB console."""

    @patch("sys.stdout", new_callable=StringIO)
    def setUp(self, mock_stdout):
        """Create all models instances for testing"""
        models_list = [
            "create BaseModel",
            "create State",
            "create User" "create Amenity",
            "create City",
            "create Review",
            "create Place",
        ]
        model = models_list[0]
        HBNBCommand().onecmd(model)

    def test_all_objects_space_notation(self):
        models_list = [
            "BaseModel",
            "State",
            "User" "Amenity",
            "City",
            "Review",
            "Place",
        ]
        for model in models_list:
            with self.subTest(model=model):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd("all"))
                    self.assertIn(model, console.getvalue().strip())

    def test_all_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_all_single_object_space_notation(self):
        """
        Test for invalid data
        """
        models_list = [
            "all BaseModel",
            "all State",
            "all User" "all Amenity",
            "all City",
            "all Review",
            "all Place",
        ]
        for model in models_list:
            with self.subTest(model=model):
                model = model.split()[1]
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(f"all {model}"))
                    self.assertIn(f"{model}", console.getvalue().strip())


if __name__ == "__main__":
    unittest.main(verbosity=2)
