#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
import datetime


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Sets up test methods."""
        FileStorage._FileStorage__objects = {}
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Smith"
        self.user.email = "email@mail.com"
        self.user.password = "password"

    def tearDown(self):
        """Tears down test methods."""
        del self.user

    def test_instantiation(self):
        """Tests instantiation of User class."""
        self.assertIsInstance(self.user, User)

    # def test_attributes(self):
    #     """Tests attributes of User class."""
    #     user_class_attr = storage.attributes()["User"]
    #     c = User()
    #     for k, v in user_class_attr.items():
    #         self.assertTrue(hasattr(c, k))
    #         self.assertEqual(type(getattr(c, k, None)), v)


    def test_unique_id(self):
        """Tests that each id is unique."""
        user2 = User()
        self.assertNotEqual(self.user.id, user2.id)

    def test_str(self):
        """Tests __str__ method of User class."""
        output = "[User] ({}) <{}>".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), output)
        self.assertIsInstance(str(self.user), str)

    def test_save(self):
        """Tests save method of User class."""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Tests to_dict method of User class."""
        self.assertEqual("to_dict" in dir(self.user), True)

    def test_kwargs(self):
        """Tests instantation of User class with kwargs."""
        user2 = User(**self.user.to_dict())
        self.assertEqual(self.user.id, user2.id)
        self.assertEqual(self.user.created_at, user2.created_at)
        self.assertEqual(self.user.updated_at, user2.updated_at)
        self.assertNotEqual(self.user, user2)

    def test_type(self):
        """Tests types of attributes."""
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def test_save(self):
        """Tests save method of User class."""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)


if __name__ == "__main__":
    unittest.main()
