#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Testing Aminty class """

    def __init__(self, *args, **kwargs):
        """ Constructor for test_Amenity class
        Args:
            args: Arguments
            kwargs: Keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test name attribute v2 """
        new = self.value()
        self.assertEqual(type(new.name), str)
