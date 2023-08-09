#!/usr/bin/python3
"""
Test File Storage
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


def setUpModule():
    """Change json file for testing to avoid side effet"""
    FileStorage._FileStorage__file_path = "test_file_storage.json"


def tearDownModule():
    """Change json file to the default"""
    import os

    try:
        file = FileStorage._FileStorage__file_path
        if os.path.isfile(file):
            os.remove(file)
    except FileNotFoundError:
        pass
    FileStorage._FileStorage__file_path = "storage_file.json"


class TestFileStorageDocstrings(unittest.TestCase):
    """Tests Docstrings"""

    @classmethod
    def setUpClass(cls):
        """Add attributs to Test class"""
        base = FileStorage()
        docs_list = []
        docs_list.append(base.__module__.__doc__)
        docs_list.append(base.__class__.__doc__)
        docs_list.append(base.all.__doc__)
        docs_list.append(base.new.__doc__)
        docs_list.append(base.save.__doc__)
        docs_list.append(base.object_classes.__doc__)
        docs_list.append(base.get_object_class.__doc__)
        docs_list.append(base.reload.__doc__)
        cls.docstrings_list = docs_list

    @classmethod
    def tearDownClass(cls):
        """Remove unused attributs docs_list from Test class"""
        del cls.docstrings_list

    def test_FileStorage_docstring(self):
        """Test docstring"""
        for docstring in self.__class__.docstrings_list:
            with self.subTest(docstring=docstring):
                self.assertTrue(len(docstring) > 10)


class TestFileStorage(unittest.TestCase):
    """Test FileStorage Class"""

    @classmethod
    def tearDownClass(cls):
        """Clean directory"""
        pass

    def test_instances(self):
        """Test Instantiation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_methodes_definition(self):
        """Test function definitions"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    def test_file_path(self):
        """Test file path"""
        obj = FileStorage()
        self.assertIsInstance(obj._FileStorage__file_path, str)

    def test_objects(self):
        """Test objects"""
        obj = FileStorage()
        self.assertIsInstance(obj._FileStorage__objects, dict)

    def test_empty_objects_when_init(self):
        """Check if objects dict is empty when inti FileStorage"""
        obj = FileStorage()
        self.assertTrue(obj._FileStorage__objects, {})

    def test_all(self):
        """Test all"""
        obj = FileStorage()
        self.assertIsInstance(obj.all(), dict)

    def test_new(self):
        """Test new"""
        obj = FileStorage()
        obj.new(BaseModel())
        self.assertTrue(obj.all())

    def test_save(self):
        """Test save"""
        obj = FileStorage()
        base = BaseModel()
        base_id = base.id
        obj.new(base)
        obj.save()
        file = FileStorage._FileStorage__file_path
        with open(file, "r") as file:
            self.assertIn(base_id, file.read())

    def test_reload(self):
        """Test reload"""
        obj = FileStorage()
        base = BaseModel()
        key = f"BaseModel.{base.id}"
        obj.new(base)
        obj.save()
        del obj.all()[key]
        obj.reload()
        self.assertIn(key, obj.all().keys())


if __name__ == "__main__":
    unittest.main(verbosity=2)
