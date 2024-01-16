#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Testing User class"""

    def __init__(self, *args, **kwargs):
        """ Constructor
        Args:
            args: Arguments
            kwargs: Keyword arguments
        Returns:
            None
        Raises:
            None
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ testing first_name attribute of User class """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ testing last_name attribute of User class and its type """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ testing email attribute of User class and its type
        and its value
        """
        new = self.value()
        self.assertEqual(type(new.email), str)
        self.assertEqual(new.email, "")

    def test_password(self):
        """ testing password attribute of User class and its type
        and its value
        """
        new = self.value()
        self.assertEqual(type(new.password), str)
        self.assertEqual(new.password, "")
