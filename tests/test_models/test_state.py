#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Testing State class"""

    def __init__(self, *args, **kwargs):
        """ Constructor for test_state class
        Args:
            args: Arguments
            kwargs: Keyword Arguments
        Return:
            None
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ testing name attribute of State class """
        new = self.value()
        self.assertEqual(type(new.name), str)
