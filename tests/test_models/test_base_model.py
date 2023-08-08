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

    def test_instantiation(self):
        """Tests BaseModel instantion"""
        base = BaseModel()
        output = "<class 'models.base_model.BaseModel'>"
        self.assertTrue(str(type(base)), output)
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_instantiation_with_args(self):
        """Tests __init__ with argument"""
        msg = 'BaseModel.__init__() takes 1 positional argument but 4 were given'
        with self.assertRaises(TypeError, msg=msg):
            base = BaseModel('1458-876-668', datetime.now(), datetime.now())

    def test_class_attributes_access(self):
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
                self.assertTrue(hasattr(ele[0], ele[1]))

    def test_class_date_attributes_type(self):
        """Tests attributes create_at, update_at types"""
        base = BaseModel()
        attrs = [
        (base.created_at, datetime),
        (base.updated_at, datetime),
        ]
        for ele in attrs:
            with self.subTest():
                self.assertIsInstance(ele[0], ele[1])

    def test_id_type(self):
        """Test class id type == string"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)

    def test_unique_id(self):
        """Confirm instances id are unique"""
        list_id = []
        max_number = 200
        for i in range(max_number):
            list_id.append(BaseModel().id)
        self.assertEqual(len(set(list_id)), max_number)




if __name__ == '__main__':
    unittest.main(verbosity=2)

# my_model = BaseModel()
# my_model.name = "My First Model"
# my_model.my_number = 89
# print(my_model)
# my_model.save()
# print(my_model)
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
