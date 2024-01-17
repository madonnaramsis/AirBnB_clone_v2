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
from models import DBStorage
import os



class test_DBStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def test_instantiation_without_errors(self):
        db_storage = DBStorage()
        self.assertEqual(str(type(db_storage)), "<class 'models.db_storage.DBStorage'>")

    def test_query_all_objects(self):
        db_storage = DBStorage()
        results = db_storage.all()
        self.assertEqual(len(results), 0)

    def test_add_object_to_session(self):
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.new(state)
        db_storage.save()
        results = db_storage.all(State)
        self.assertEqual(len(results), 1)

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
from models import DBStorage
import os



class test_DBStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def test_query_all_objects_with_class_specified(self):
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.new(state)
        db_storage.save()
        results = db_storage.all(State)
        self.assertEqual(len(results), 1)

    def test_delete_object_from_session(self):
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.new(state)
        db_storage.save()
        db_storage.delete(state)
        results = db_storage.all(State)
        self.assertEqual(len(results), 0)

    def test_add_city_to_session(self):
        db_storage = DBStorage()
        city = City(name="San Francisco", state_id=1)
        db_storage.new(city)
        db_storage.save()
        results = db_storage.all(City)
        self.assertEqual(len(results), 1)

    def test_query_objects_with_class_specified(self):
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.new(state)
        db_storage.save()
        results = db_storage.all(State)
        self.assertEqual(len(results), 1)

    def test_delete_nonexistent_object(self):
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.delete(state)
        db_storage.save()
        results = db_storage.all(State)
        self.assertEqual(len(results), 0)

    def test_reload_without_creating_tables(self):
        db_storage = DBStorage()
        db_storage.reload()
        results = db_storage.all(State)
        self.assertEqual(len(results), 0)

    def test_reload_with_creating_tables(self):
        db_storage = DBStorage()
        db_storage.reload()
        results = db_storage.all(State)
        self.assertEqual(len(results), 0)

    def test_add_object_to_session(self):
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.new(state)
        db_storage.save()
        results = db_storage.all(State)
        self.assertEqual(len(results), 1)

    def test_query_all_objects(self):
        db_storage = DBStorage()
        results = db_storage.all()
        self.assertEqual(len(results), 0)

    def test_add_object_to_session(self):
        db_storage = DBStorage()
        state = State(name="California")
        db_storage.new(state)
        db_storage.save()
        results = db_storage.all(State)
        self.assertEqual(len(results), 1)
