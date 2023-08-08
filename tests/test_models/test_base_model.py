#!/usr/bin/python3
"""
Unit test for BaseModel class
"""

import unittest
from models.base_model import BaseModel


class TestBaseModelClassDocstrings(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
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
        del cls.docs_list

    def test_module_docstring(self):
        for docstring in self.__class__.docs_list:
            with self.subTest(docstring=docstring):
                self.assertTrue(len(docstring) > 10)


class TestBaseClass(unittest.TestCase):
    

    def test_init_object(self):
        base = BaseModel()
        self.assertTrue(base.id)



if __name__ == '__main__':
    unittest.main()

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
