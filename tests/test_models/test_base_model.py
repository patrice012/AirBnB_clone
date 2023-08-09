#!/usr/bin/python3
"""
Unit test for BaseModel class
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelDocstrings(unittest.TestCase):
    """Tests Docstrings"""

    @classmethod
    def setUpClass(cls):
        """Add attributs to Test class"""
        base = BaseModel()
        docs_list = []
        docs_list.append(base.__module__.__doc__)
        docs_list.append(base.__class__.__doc__)
        docs_list.append(base.__str__.__doc__)
        docs_list.append(base.__init__.__doc__)
        docs_list.append(base.save.__doc__)
        docs_list.append(base.to_dict.__doc__)
        cls.docstrings_list = docs_list

    @classmethod
    def tearDownClass(cls):
        """Remove unused attributs from Test class"""
        del cls.docstrings_list

    def test_BaseModel_docstring(self):
        """Test docstring"""
        for docstring in self.__class__.docstrings_list:
            with self.subTest(docstring=docstring):
                self.assertTrue(len(docstring) > 10)


class TestBaseClass(unittest.TestCase):
    """Tests BaseClass"""

    RUN_WITH_ARGS = True

    def setUp(self):
        """Provide initial object for most tests"""
        self.base = BaseModel()

    def tearDown(self):
        """Remove unused varaiables"""
        del self.base

    def test_instantiation(self):
        """Tests BaseModel instantion"""
        output = "<class 'models.base_model.BaseModel'>"
        self.assertTrue(str(type(self.base)), output)
        self.assertIsInstance(self.base, BaseModel)
        self.assertTrue(issubclass(type(self.base), BaseModel))

    @unittest.skipIf(RUN_WITH_ARGS, "__init__ has now arg and kwargs")
    def test_instantiation_with_args(self):
        """Tests __init__ with argument"""
        m = "BaseModel.__init__() takes 1 positional argument but 4 were given"
        with self.assertRaises(TypeError, msg=m):
            base = BaseModel("1458-876-668", datetime.now(), datetime.now())

    def test_class_attributes_access(self):
        """Tests attributes id, create_at, update_at"""
        attrs = [
            (self.base, "id"),
            (self.base, "created_at"),
            (self.base, "updated_at"),
            (self.base, "save"),
            (self.base, "to_dict"),
        ]
        for ele in attrs:
            with self.subTest():
                self.assertTrue(hasattr(ele[0], ele[1]))

    def test_class_date_attributes_type(self):
        """Tests attributes create_at, update_at types"""
        attrs = [
            (self.base.created_at, datetime),
            (self.base.updated_at, datetime),
        ]
        for ele in attrs:
            with self.subTest():
                self.assertIsInstance(ele[0], ele[1])

    def test_id_type(self):
        """Test class id type == string"""
        self.assertIsInstance(self.base.id, str)

    def test_unique_id(self):
        """Confirm instances id are unique"""
        list_id = []
        max_number = 200
        for i in range(max_number):
            list_id.append(BaseModel().id)
        self.assertEqual(len(set(list_id)), max_number)

    def test_str_method_output(self):
        """Test custom str method behavior"""
        base = self.base
        name = type(base).__name__
        output = "[{}] ({}) <{}>".format(name, base.id, base.__dict__)
        self.assertEqual(str(base), output)
        self.assertEqual(base.__str__(), output)

    def test_save_method(self):
        """
        Test save method
        update of updated_at instance attr
        """
        base = self.base
        date_1 = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, date_1)

    def test_save_method_multiple_times(self):
        """
        Test save method
        update of updated_at instance attr
        """
        base = BaseModel()
        list_date = [base.updated_at]
        max_number = 500
        for i in range(1, max_number):
            base.save()
            list_date.append(base.updated_at)
        self.assertEqual(len(set(list_date)), max_number)

    def test_to_dict(self):
        """
        Test instance method to_dict
        """
        base_to_dict = self.base.to_dict()
        self.assertEqual(base_to_dict["__class__"], "BaseModel")
        self.assertEqual(type(base_to_dict["created_at"]), str)
        self.assertEqual(type(base_to_dict["updated_at"]), str)

    # Test for __init__ with args and kwargs
    def test_init_with_many_args(self):
        """Tests instantiation with many args"""
        # self.clearStorageSystem()
        base_1 = BaseModel([i for i in range(1000)])
        base_2 = BaseModel(set([i for i in range(1000)]))
        base_3 = BaseModel(tuple([i for i in range(1000)]))
        output = "<class 'models.base_model.BaseModel'>"
        list_obj = [(base_1,), (base_2,), (base_3,)]
        for obj in list_obj:
            with self.subTest():
                self.assertEqual(str(type(obj[0])), output)
                self.assertIsInstance(obj[0], BaseModel)

    def test_init_with_invalid_keys_using_kwargs(self):
        """Tests instantiation with many kwargs"""
        # self.clearStorageSystem()
        base_1 = BaseModel(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)
        base_2 = BaseModel(**{"a": 1, "b": 2, "c": 3, "d": 4})
        output = "<class 'models.base_model.BaseModel'>"
        list_obj = [(base_1,), (base_2,)]
        for obj in list_obj:
            with self.subTest():
                self.assertEqual(str(type(obj[0])), output)
                self.assertIsInstance(obj[0], BaseModel)

    def test_init_with_valid_keys_using_kwargs(self):
        """Tests instantiation with valid kwargs"""
        # self.clearStorageSystem()
        data = {
            "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "created_at": "2017-09-28T21:03:54.052298",
            "__class__": "BaseModel",
            "updated_at": "2017-09-28T21:03:54.052302",
        }
        base = BaseModel(**data)
        output = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(base)), output)
        self.assertIsInstance(base, BaseModel)

    def test_init_with_kwargs_and_adding_extra_keys(self):
        """Tests instantiation with many extrat keys"""
        # self.clearStorageSystem()
        data = {
            "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "created_at": "2017-09-28T21:03:54.052298",
            "__class__": "BaseModel",
            "my_number": 89,
            "updated_at": "2017-09-28T21:03:54.052302",
            "name": "My_First_Model",
            "valid": True,
            "format": "Dict",
        }
        base = BaseModel(**data)
        for key in data.keys():
            if key != "__class__":
                self.assertTrue(hasattr(base, key))

    def test_init_from_instance_dict(self):
        """Tests init from dictionary"""
        base = BaseModel()
        base_dict = base.to_dict()
        base_2 = BaseModel(**base_dict)
        self.assertEqual(base.id, base_2.id)
        self.assertEqual(base.created_at, base_2.created_at)
        self.assertEqual(base.updated_at, base_2.updated_at)
        self.assertEqual(base.__dict__, base_2.__dict__)


if __name__ == "__main__":
    unittest.main(verbosity=2)
