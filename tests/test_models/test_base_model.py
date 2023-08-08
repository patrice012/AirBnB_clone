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
        _cls = BaseModel()
        docs_list = []
        docs_list.append(_cls.__module__.__doc__)
        docs_list.append(_cls.__class__.__doc__)
        docs_list.append(_cls.__str__.__doc__)
        docs_list.append(_cls.__init__.__doc__)
        docs_list.append(_cls.save.__doc__)
        docs_list.append(_cls.to_dict.__doc__)
        cls.docs_list = docs_list

    @classmethod
    def tearDownClass(cls):
        """Remove unused attributs from Test class"""
        del cls.docs_list

    def test_module_docstring(self):
        """Test docstring"""
        for docstring in self.__class__.docs_list:
            with self.subTest(docstring=docstring):
                self.assertTrue(len(docstring) > 10)


class TestBaseClass(unittest.TestCase):
    """Tests BaseClass"""

    def test_instantiation(self):
        """Tests BaseModel instantion"""
        base = BaseModel()
        self.assertTrue(str(type(base)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(issubclass(type(base)), BaseModel)

    def test_instantiation_with_args(self):
        """Tests __init__ with argument"""
        msg = 'BaseModel.__init__() takes 1 positional argument but 4 were given'
        with self.assertRaises(TypeEror, msg=msg):
            base = BaseModel('1458-876-668', datetime.now(), datetime.now())

    def test_class_attributes(self):
        """Tests attributes id, create_at, update_at"""
        base = BaseModel()
        attrs = [
        (base, 'id'),
        (base, 'created_at'),
        (base, 'updated_at'),
        (base, 'save'),
        (base, 'to_dict')
        ]
        for ele in attrs:
            with self.subTest():
                self.assertTrue(hasattr(ele[0]), ele[1])



if __name__ == '__main__':
    unittest.main(verbosity=2)
