#!/usr/bin/python3
"""This module defines class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines user attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
