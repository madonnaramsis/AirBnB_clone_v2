#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class representing a feature or service in a facility."""
    name = ""
