#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.db_storage import DBStorage




class test_DBStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def test_instantiation_without_errors(self):
        """ test instantiation of the DBStorage class """
        db_storage = DBStorage()
        self.assertEqual(str(type(db_storage)), "<class 'models.db_storage.DBStorage'>")

    def test_query_all_objects(self):
        """ test the query all method """
        db_storage = DBStorage()
        results = db_storage.all()
        self.assertEqual(len(results), 0)

    def test_add_object_to_session(self):
        """ test the add method """
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.new(state)
        db_storage.save()
        results = db_storage.all(State)
        self.assertEqual(len(results), 1)

    def test_query_all_objects_with_class_specified(self):
        """ test the query all method """
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.new(state)
        db_storage.save()
        results = db_storage.all(State)
        self.assertEqual(len(results), 1)

    def test_delete_object_from_session(self):
        """ test the delete method """
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.new(state)
        db_storage.save()
        db_storage.delete(state)
        results = db_storage.all(State)
        self.assertEqual(len(results), 0)

    def test_add_city_to_session(self):
        """ test the add method """
        db_storage = DBStorage()
        city = City(name="San Francisco", state_id=1)
        db_storage.new(city)
        db_storage.save()
        results = db_storage.all(City)
        self.assertEqual(len(results), 1)

    def test_query_objects_with_class_specified(self):
        """ test the query all method """
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.new(state)
        db_storage.save()
        results = db_storage.all(State)
        self.assertEqual(len(results), 1)

    def test_delete_nonexistent_object(self):
        """test deleting nonexistent object"""
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.delete(state)
        db_storage.save()
        results = db_storage.all(State)
        self.assertEqual(len(results), 0)

    def test_reload_without_creating_tables(self):
        """test reloading without creating tables"""
        db_storage = DBStorage()
        db_storage.reload()
        results = db_storage.all(State)
        self.assertEqual(len(results), 0)

    def test_reload_with_creating_tables(self):
        """test reloading with creating tables"""
        db_storage = DBStorage()
        db_storage.reload()
        results = db_storage.all(State)
        self.assertEqual(len(results), 0)
        db_storage.new(State(name="California"))
        db_storage.save()
        db_storage.reload()
        results = db_storage.all(State)
        self.assertEqual(len(results), 1)

    def test_add_amenity_to_session(self):
        """ test the add method """
        db_storage = DBStorage()
        amenity = Amenity(name="Wifi")
        db_storage.new(amenity)
        db_storage.save()
        results = db_storage.all(Amenity)
        self.assertEqual(len(results), 1)

    def test_delete_already_deleted_object(self):
        """test deleting already deleted object"""
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.new(state)
        db_storage.save()
        db_storage.delete(state)
        db_storage.delete(state)
        results = db_storage.all(State)
        self.assertEqual(len(results), 0)
