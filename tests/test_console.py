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
    if DEBUG and file:
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

    def test_help(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help"))
            output = "Documented commands (type help <topic>):"
            self.assertIn(output, console.getvalue())

    def test_functions_in_help_command(self):
        list_of_function = [
            "EOF",
            "create",
            "show",
            "all",
            "destroy",
            "count",
            "help",
            "quit",
        ]
        with patch("sys.stdout", new=StringIO()) as console:
            HBNBCommand().onecmd("help")
            for function in list_of_function:
                with self.subTest():
                    self.assertIn(function, console.getvalue())

    def test_help_quit(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertTrue(console.getvalue().strip())

    def test_help_create(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertTrue(console.getvalue().strip())

    def test_help_update(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertTrue(console.getvalue().strip())

    def test_help_EOF(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertTrue(console.getvalue().strip())

    def test_help_count(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertTrue(console.getvalue().strip())

    def test_help_show(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertTrue(console.getvalue().strip())

    def test_help_all(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertTrue(console.getvalue().strip())

    def test_help_destroy(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertTrue(console.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Tests for exiting the HBNB console."""

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertTrue(HBNBCommand().onecmd("quit"))


class TestHBNBCommand_create(unittest.TestCase):
    """Tests for create command of the HBNB console."""

    @classmethod
    def setUpClass(cls):
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        file = FileStorage._FileStorage__file_path
        if file:
            remove_file(file)

    def test_create_object(self):
        models_list = [
            "create BaseModel",
            "create Review",
            "create User",
            "create Place",
            "create Amenity",
            "create City",
            "create State",
        ]
        for prompt in models_list:
            with self.subTest():
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    self.assertLess(0, len(console.getvalue().strip()))
                    Klass = prompt.split(" ")[1]
                    test_k = "{}.{}".format(Klass, console.getvalue().strip())
                    self.assertIn(test_k, storage.all().keys())

    def test_create_using_dot_notation(self):
        models_list = [
            "BaseModel.create()",
            "Review.create()",
            "User.create()",
            "Place.create()",
            "Amenity.create()",
            "City.create()",
            "BaseModel.create()",
        ]
        for prompt in models_list:
            with self.subTest():
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    self.assertLess(0, len(console.getvalue().strip()))
                    Klass = prompt.split(" ")[1]
                    test_k = "{}.{}".format(Klass, console.getvalue().strip())
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

    def test_create_using_dot_notation(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(".create()"))
            self.assertEqual(expected, console.getvalue().strip())

        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(expected, console.getvalue().strip())


class TestHBNBCommand_show(unittest.TestCase):
    """Tests for show command of the HBNB console"""

    @classmethod
    def setUpClass(cls):
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        file = FileStorage._FileStorage__file_path
        if file:
            remove_file(file)

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
            "show User",
            "show Amenity",
            "show City",
            "show Review",
            "show Place",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    self.assertEqual(expected, console.getvalue().strip())

    def test_show_missing_id_dot_notation(self):
        expected = "** instance id missing **"
        models_list = [
            "BaseModel.show()",
            "State.show()",
            "User.show()",
            "Amenity.show()",
            "City.show()",
            "Review.show()",
            "Place.show()",
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
            "show User 1",
            "show Amenity 1",
            "show City 1",
            "show Review 1",
            "show Place 1",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    self.assertEqual(expected, console.getvalue().strip())

    def test_show_no_instance_found_dot_notation(self):
        expected = "** no instance found **"
        models_list = [
            "BaseModel.show(1)",
            "State.show(1)",
            "User.show(1)",
            "Amenity.show(1)",
            "City.show(1)",
            "Review.show(1)",
            "Place.show(1)",
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
            "create User",
            "create Amenity",
            "create City",
            "create Review",
            "create Place",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    object_id = console.getvalue().strip()
                model = prompt.split()[1]
                with patch("sys.stdout", new=StringIO()) as console:
                    obj = storage.all()["{}.{}".format(model, object_id)]
                    command = "show {} {}".format(model, object_id)
                    self.assertFalse(HBNBCommand().onecmd(command))
                    self.assertEqual(obj.__str__(), console.getvalue().strip())

    def test_show_objects_dot_notation(self):
        models_list = [
            "create BaseModel",
            "create State",
            "create User",
            "create Amenity",
            "create City",
            "create Review",
            "create Place",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    object_id = console.getvalue().strip()
                model = prompt.split()[1]
                with patch("sys.stdout", new=StringIO()) as console:
                    obj = storage.all()["{}.{}".format(model, object_id)]
                    command = "{}.{}({})".format(model, "show", object_id)
                    self.assertFalse(HBNBCommand().onecmd(command))
                    self.assertEqual(obj.__str__(), console.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Tests for destroy command of the HBNB console."""

    @patch("sys.stdout", new_callable=StringIO)
    def setUp(self, mock_stdout):
        """Create all models instances for testing"""
        models_list = [
            "create BaseModel",
            "create State",
            "create User",
            "create Amenity",
            "create City",
            "create Review",
            "create Place",
        ]
        for model in models_list:
            HBNBCommand().onecmd(model)

    def test_destroy_missing_class_space_notation(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_missing_class_dot_notation(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(".destroy"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_invalid_class_using_dot_notation(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_id_missing_space_notation(self):
        expected = "** instance id missing **"
        models_list = [
            "destroy BaseModel",
            "destroy State",
            "destroy User",
            "destroy Amenity",
            "destroy City",
            "destroy Review",
            "destroy Place",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_id_missing_dot_notation(self):
        expected = "** instance id missing **"
        models_list = [
            "destroy BaseModel",
            "destroy State",
            "destroy User",
            "destroy Amenity",
            "destroy City",
            "destroy Review",
            "destroy Place",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    func, Klass = prompt.split(" ")
                    _input = f"{Klass.strip()}.{func.strip()}()"
                    self.assertFalse(HBNBCommand().onecmd(_input))
                    self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_invalid_id_space_notation(self):
        expected = "** no instance found **"
        models_list = [
            "destroy BaseModel 1",
            "destroy State 1",
            "destroy User 1",
            "destroy Amenity 1",
            "destroy City 1",
            "destroy Review 1",
            "destroy Place 1",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_invalid_id_dot_notation(self):
        expected = "** no instance found **"
        models_list = [
            "destroy BaseModel 1",
            "destroy State 1",
            "destroy User 1",
            "destroy Amenity 1",
            "destroy City 1",
            "destroy Review 1",
            "destroy Place 1",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    func, Klass, _id = prompt.split(" ")
                    _input = f"{Klass.strip()}.{func.strip()}({_id.strip()})"
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    self.assertEqual(expected, console.getvalue().strip())

    def test_destroy_objects_space_notation(self):
        models_list = [
            "create BaseModel",
            "create State",
            "create User",
            "create Amenity",
            "create City",
            "create Review",
            "create Place",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    object_id = console.getvalue().strip()
                model = prompt.split()[1]

                with patch("sys.stdout", new=StringIO()) as console:
                    obj = storage.all()["{}.{}".format(model, object_id)]
                    command = "destroy {} {}".format(model, object_id)
                    self.assertFalse(HBNBCommand().onecmd(command))
                    self.assertNotIn(obj, storage.all())

    def test_destroy_objects_dot_notation(self):
        models_list = [
            "create BaseModel",
            "create State",
            "create User",
            "create Amenity",
            "create City",
            "create Review",
            "create Place",
        ]
        for prompt in models_list:
            with self.subTest(prompt=prompt):
                with patch("sys.stdout", new=StringIO()) as console:
                    self.assertFalse(HBNBCommand().onecmd(prompt))
                    object_id = console.getvalue().strip()
                model = prompt.split()[1]

                with patch("sys.stdout", new=StringIO()) as console:
                    obj = storage.all()["{}.{}".format(model, object_id)]
                    command = "{}.destroy({})".format(model, object_id)
                    self.assertFalse(HBNBCommand().onecmd(command))
                    self.assertNotIn(obj, storage.all())


class TestHBNBCommand_all(unittest.TestCase):
    """Tests for all command of the HBNB console."""

    @classmethod
    def setUpClass(cls):
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        file = FileStorage._FileStorage__file_path
        if file:
            remove_file(file)

    @patch("sys.stdout", new_callable=StringIO)
    def setUp(self, mock_stdout):
        """Create all models instances for testing"""
        models_list = [
            "create BaseModel",
            "create State",
            "create User",
            "create Amenity",
            "create City",
            "create Review",
            "create Place",
        ]
        for model in models_list:
            HBNBCommand().onecmd(model)

    def test_all_objects_space_notation(self):
        models_list = [
            "BaseModel",
            "State",
            "User",
            "Amenity",
            "City",
            "Review",
            "Place",
        ]
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all"))
            for model in models_list:
                with self.subTest(model=model):
                    self.assertIn(model, console.getvalue().strip())

    def test_single_class_objects_dot_notation(self):
        models_list = [
            "BaseModel",
            "State",
            "User",
            "Amenity",
            "City",
            "Review",
            "Place",
        ]
        with patch("sys.stdout", new=StringIO()) as console:
            for Klass in models_list:
                with self.subTest():
                    self.assertFalse(HBNBCommand().onecmd(f"all.{Klass}"))
                    self.assertGreaterEqual(len(console.getvalue().strip()), 1)

    def test_single_class_objects_space_notation(self):
        """
        Test for invalid data
        """
        models_list = [
            "all BaseModel",
            "all State",
            "all User",
            "all Amenity",
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

    def test_all_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(expected, console.getvalue().strip())


class TestHBNBCommand_update(unittest.TestCase):
    """Test Update fonction"""

    @classmethod
    def setUpClass(cls):
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        file = FileStorage._FileStorage__file_path
        if file:
            remove_file(file)

    def setUp(self):
        objects_mapping = {}
        models_list = [
            "create BaseModel",
            "create State",
            "create User",
            "create Amenity",
            "create City",
            "create Review",
            "create Place",
        ]
        for prompt in models_list:
            with patch("sys.stdout", new=StringIO()) as console:
                HBNBCommand().onecmd(prompt)
                object_id = console.getvalue().strip()
                Klass = prompt.split(" ")[1].strip()
                objects_mapping[Klass] = object_id
        self.objects_mapping = objects_mapping
        self.models_list = models_list

    def tearDown(self):
        del self.objects_mapping
        del self.models_list

    def test_update_class_missing_using_space_noation(self):
        output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_class_missing_using_dot_noation(self):
        output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_invalid_class_space_notation(self):
        output = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_invalid_class_dot_notation(self):
        output = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_id_missing_space_notation(self):
        output = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_id_missing_dot_notation(self):
        output = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update()"))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_instance_not_found_using_space_notation(self):
        output = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 121212"))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_instance_not_found_missing_dot_notation(self):
        output = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as console:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update(121212)"))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_attribute_name_missing_using_space_notation(self):
        output = "** attribute name missing **"
        obj_id = self.objects_mapping["BaseModel"]
        with patch("sys.stdout", new=StringIO()) as console:
            _input = f"update BaseModel {obj_id}"
            self.assertFalse(HBNBCommand().onecmd(_input))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_attribute_name_missing_dot_notation(self):
        output = "** attribute name missing **"
        obj_id = self.objects_mapping["BaseModel"]
        with patch("sys.stdout", new=StringIO()) as console:
            _input = f"BaseModel.update({obj_id})"
            self.assertFalse(HBNBCommand().onecmd(_input))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_value_for_attribute_missing_using_space_notation(self):
        output = "** attribute name missing **"
        obj_id = self.objects_mapping["BaseModel"]
        with patch("sys.stdout", new=StringIO()) as console:
            _input = f"update BaseModel {obj_id} test"
            self.assertFalse(HBNBCommand().onecmd(_input))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_value_for_attribute_missing_using_dot_notation(self):
        output = "** attribute name missing **"
        obj_id = self.objects_mapping["BaseModel"]
        with patch("sys.stdout", new=StringIO()) as console:
            _input = f"BaseModel.update({obj_id} test)"
            self.assertFalse(HBNBCommand().onecmd(_input))
            self.assertTrue(output, console.getvalue().strip())

    def test_update_for_all_classes_using_space_notation(self):
        models_list = self.models_list
        for model in models_list:
            Klass = model.split(" ")[1].strip()
            _id = self.objects_mapping[Klass]
            _input = f"update {Klass} {_id} email aibnb@mail.com"
            with patch("sys.stdout", new=StringIO()) as console:
                HBNBCommand().onecmd(_input)
                test_dict = storage.all()[f"{Klass}.{_id}"].__dict__
                self.assertTrue("email" in test_dict.keys())
                self.assertEqual(test_dict["email"], "aibnb@mail.com")

    def test_update_for_all_classes_using_dot_notation(self):
        models_list = self.models_list
        for model in models_list:
            Klass = model.split(" ")[1].strip()
            _id = self.objects_mapping[Klass]
            _input = f"{Klass}.update({_id} test alx-se)"
            with patch("sys.stdout", new=StringIO()) as console:
                HBNBCommand().onecmd(_input)
                test_dict = storage.all()[f"{Klass}.{_id}"].__dict__
                self.assertTrue("test" in test_dict.keys())
                self.assertEqual(test_dict["test"], "alx-se")

    def test_update_for_all_classes_using_dict_space_notation(self):
        for model in self.models_list:
            Klass = model.split(" ")[1].strip()
            _id = self.objects_mapping[Klass]
            attr_dict = {"first_name": "John", "age": 89}
            _input = f"update {Klass} {_id} {attr_dict}"
            with patch("sys.stdout", new=StringIO()) as console:
                HBNBCommand().onecmd(_input)
                test_dict = storage.all()[f"{Klass}.{_id}"].__dict__
                with self.subTest():
                    for key, value in attr_dict.items():
                        self.assertTrue(key in test_dict.keys())
                        self.assertEqual(test_dict[key], value)

    def test_update_for_all_classes_using_dict_dot_notation(self):
        for model in self.models_list:
            Klass = model.split(" ")[1].strip()
            _id = self.objects_mapping[Klass]
            attr_dict = {"first_name": "John", "age": 89}
            _input = f"{Klass}.update({_id} {attr_dict})"
            with patch("sys.stdout", new=StringIO()) as console:
                HBNBCommand().onecmd(_input)
                test_dict = storage.all()[f"{Klass}.{_id}"].__dict__
                with self.subTest():
                    for key, value in attr_dict.items():
                        self.assertTrue(key in test_dict.keys())
                        self.assertEqual(test_dict[key], value)


if __name__ == "__main__":
    unittest.main(verbosity=2)
