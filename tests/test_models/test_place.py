import unittest
from models.place import Place
"""Place Class Unittest"""


class TestPlace(unittest.TestCase):
    """TestPlace Class"""
    def setUp(self):
        """Sets up Place for testing"""
        self.place = Place()

    def test_place_type(self):
        """Tests place type"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_place_name(self):
        """Tests place name"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_id(self):
        """Tests place id"""
        self.assertEqual(type(self.place.id), str)

    def test_place_created_at(self):
        """Tests place created_at"""
        self.assertEqual(type(self.place.created_at).__name__, "datetime")

    def test_place_updated_at(self):
        """Tests place updated_at"""
        self.assertEqual(type(self.place.updated_at).__name__, "datetime")

    def test_place_str(self):
        """Tests place __str__"""
        self.assertEqual(type(self.place.__str__()), str)

    def test_place_save(self):
        """Tests place save"""
        self.place.save()
        self.assertEqual(type(self.place.updated_at).__name__, "datetime")

    def test_place_to_dict(self):
        """Tests place to_dict"""
        self.assertEqual(type(self.place.to_dict()), dict)

    def test_place_kwargs(self):
        """Tests place kwargs"""
        self.new_place = Place(name="San Francisco")
        self.assertEqual(type(self.new_place).__name__, "Place")
        self.assertTrue(hasattr(self.new_place, "name"))
        self.assertEqual(self.new_place.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()
