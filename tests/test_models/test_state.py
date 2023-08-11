import unittest
from models.state import State
"""State Class Tests"""


class TestState(unittest.TestCase):
    """TestState Class"""
    def setUp(self):
        """Sets up State for testing"""
        self.state = State()

    def test_state_type(self):
        """Tests state type"""
        self.assertEqual(type(self.state.name), str)

    def test_state_name(self):
        """Tests state name"""
        self.assertEqual(self.state.name, "")

    def test_state_id(self):
        """Tests state id"""
        self.assertEqual(type(self.state.id), str)

    def test_state_created_at(self):
        """Tests state created_at"""
        self.assertEqual(type(self.state.created_at).__name__, "datetime")

    def test_state_updated_at(self):
        """Tests state updated_at"""
        self.assertEqual(type(self.state.updated_at).__name__, "datetime")

    def test_state_str(self):
        """Tests state __str__"""
        self.assertEqual(type(self.state.__str__()), str)

    def test_state_save(self):
        """Tests state save"""
        self.state.save()
        self.assertEqual(type(self.state.updated_at).__name__, "datetime")

    def test_state_to_dict(self):
        """Tests state to_dict"""
        self.assertEqual(type(self.state.to_dict()), dict)

    def test_state_kwargs(self):
        """Tests state kwargs"""
        self.new_state = State(name="California")
        self.assertEqual(type(self.new_state).__name__, "State")
        self.assertTrue(hasattr(self.new_state, "name"))
        self.assertEqual(self.new_state.name, "California")


if __name__ == "__main__":
    unittest.main()
