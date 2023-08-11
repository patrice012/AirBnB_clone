import unittest
from models.city import City
"""City Class Tests"""


class TestCity(unittest.TestCase):
    """TestCity Class"""
    def setUp(self):
        """Sets up City for testing"""
        self.city = City()

    def test_city_type(self):
        """Tests city type"""
        self.assertEqual(type(self.city.name), str)

    def test_city_name(self):
        """Tests city name"""
        self.assertEqual(self.city.name, "")

    def test_city_id(self):
        """Tests city id"""
        self.assertEqual(type(self.city.id), str)

    def test_city_created_at(self):
        """Tests city created_at"""
        self.assertEqual(type(self.city.created_at).__name__, "datetime")

    def test_city_updated_at(self):
        """Tests city updated_at"""
        self.assertEqual(type(self.city.updated_at).__name__, "datetime")

    def test_city_str(self):
        """Tests city __str__"""
        self.assertEqual(type(self.city.__str__()), str)

    def test_city_save(self):
        """Tests city save"""
        self.city.save()
        self.assertEqual(type(self.city.updated_at).__name__, "datetime")

    def test_city_to_dict(self):
        """Tests city to_dict"""
        self.assertEqual(type(self.city.to_dict()), dict)

    def test_city_kwargs(self):
        """Tests city kwargs"""
        self.new_city = City(name="San Francisco")
        self.assertEqual(type(self.new_city).__name__, "City")
        self.assertTrue(hasattr(self.new_city, "name"))
        self.assertEqual(self.new_city.name, "San Francisco")


if __name__ == "__main__":
    unittest.main()
