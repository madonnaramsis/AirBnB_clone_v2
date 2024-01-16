#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Testing City class"""

    def __init__(self, *args, **kwargs):
        """Constructor
        Args:
            args: Arguments
            kwargs: Keyword arguments
        Returns:
            None
        Raises:
            None
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ testing state_id attribute of City class """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ testing name attribute of City class """
        new = self.value()
        self.assertEqual(type(new.name), str)
