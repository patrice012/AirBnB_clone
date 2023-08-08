#!/usr/bin/python3
"""
Unit test for BaseModel class
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelClassDocstrings(unittest.TestCase):
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

    def test_module_docstring(self):
        """Test docstring"""
        for docstring in self.__class__.docstrings_list:
            with self.subTest(docstring=docstring):
                self.assertTrue(len(docstring) > 10)


class TestBaseClass(unittest.TestCase):
    """Tests BaseClass"""

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

    def test_instantiation_with_args(self):
        """Tests __init__ with argument"""
        msg = 'BaseModel.__init__() takes 1 positional argument but 4 were given'
        with self.assertRaises(TypeError, msg=msg):
            base = BaseModel('1458-876-668', datetime.now(), datetime.now())

    def test_class_attributes_access(self):
        """Tests attributes id, create_at, update_at"""
        attrs = [
        (self.base, 'id'),
        (self.base, 'created_at'),
        (self.base, 'updated_at'),
        (self.base, 'save'),
        (self.base, 'to_dict')
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
        output = "[{}] ({}) <{}>".format(type(base).__name__, base.id, base.__dict__)
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



if __name__ == '__main__':
    unittest.main(verbosity=2)
