#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Testing Basemodel class"""

    def __init__(self, *args, **kwargs):
        """Constructor for test_basemodel class
        Args:
            args: Arguments
            kwargs: Keyword arguments
        Returns:
            None
        """
        """ Constructor for test_basemodel class
        Args:
            args: Arguments
            kwargs: Keyword arguments
        Returns:
            None
        """
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Testing teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_default(self):
        """testing default values"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """testing kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """testing kwargs with int value"""
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
        """testing string output"""
        i = self.value()
        self.assertEqual(str(i), "[{}] ({}) {}".format(
            self.name, i.id, i.__dict__))

    def test_todict(self):
        """testing to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """testing kwargs with none value"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """testing kwargs with one argument"""
        n = {"Name": "test"}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """testing id value and type"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """testing created_at value and type"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """testing updated_at value and type,
        checking if created_at != updated_at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_set_single_attribute(self):
        """Can set a single attribute with a valid key-value pair"""
        obj = BaseModel()
        obj.set(attribute="value")
        self.assertEqual(obj.attribute, "value")

    def test_set_multiple_attributes(self):
        """Can set multiple attributes with valid key-value pairs"""
        obj = BaseModel()
        obj.set(attribute1="value1", attribute2="value2")
        self.assertEqual(obj.attribute1, "value1")
        self.assertEqual(obj.attribute2, "value2")

    def test_set_integer_attributes(self):
        """Can set attributes with integer values"""
        obj = BaseModel()
        obj.set(attribute1=10, attribute2=20)
        self.assertEqual(obj.attribute1, 10)
        self.assertEqual(obj.attribute2, 20)
