#!/usr/bin/python3
""" City hbnb projrct module """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains id and name"""
    state_id = ""
    name = ""
