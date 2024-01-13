#!/usr/bin/python3
""" Review module for the `project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store """
    place_id = ""
    user_id = ""
    text = ""
