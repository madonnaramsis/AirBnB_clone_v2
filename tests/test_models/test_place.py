#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Testing Place class"""

    def __init__(self, *args, **kwargs):
        """ Constructor
        Args:
            args: Arguments
            kwargs: Keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ testing city_id attribute of Place class """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ testing user_id attribute of Place class and its type """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """testing name attribute of Place class and its type and its value"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ testing description attribute of Place class and its type"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ testing number_rooms attribute of Place class and its type """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ testing number_bathrooms attribute of Place class and its type """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ testing max_guest attribute of Place class and its type """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ testing price_by_night attribute of Place class and its type """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ testing latitude attribute of Place class and its type """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ testing longitude attribute of Place class and its type """
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ testing amenity_ids attribute of Place class and its type """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
