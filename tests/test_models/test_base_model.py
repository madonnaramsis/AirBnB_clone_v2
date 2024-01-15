#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Testing save"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open("file.json", "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), "[{}] ({}) {}".format(self.name, i.id, i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {"Name": "test"}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_set_single_attribute(self):
        obj = BaseModel()
        obj.set(attribute="value")
        assert obj.attribute == "value"

    # Can set multiple attributes with valid key-value pairs
    def test_set_multiple_attributes(self):
        obj = BaseModel()
        obj.set(attribute1="value1", attribute2="value2")
        assert obj.attribute1 == "value1"
        assert obj.attribute2 == "value2"

    # Can set attributes with integer values
    def test_set_integer_attributes(self):
        obj = BaseModel()
        obj.set(attribute1=10, attribute2=20)
        assert obj.attribute1 == 10
        assert obj.attribute2 == 20

    # Does not set 'id' attribute
    def test_does_not_set_id_attribute(self):
        obj = BaseModel()
        obj.set(id="123")
        assert not hasattr(obj, "id")

    # Does not set attribute with key containing 'id'
    def test_does_not_set_attribute_with_id_in_key(self):
        obj = BaseModel()
        obj.set(attribute_id="123")
        assert not hasattr(obj, "attribute_id")

    # Does not set attribute with invalid key
    def test_does_not_set_attribute_with_invalid_key(self):
        obj = BaseModel()
        obj.set("invalid_key", "value")
        assert not hasattr(obj, "invalid_key")
