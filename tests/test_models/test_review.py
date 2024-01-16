#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Testing review class"""

    def __init__(self, *args, **kwargs):
        """ Constructor for test_review class
        Args:
            args: Arguments for the base class
            kwargs: Keyword arguments for the base class
        Returns:
            None
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ testing place_id attribute of the class """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ testing user_id attribute of the class """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ testing text attribute of the class """
        new = self.value()
        self.assertEqual(type(new.text), str)
