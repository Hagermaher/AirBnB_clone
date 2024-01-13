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
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        h = self.value()
        self.assertEqual(type(h), self.value)

    def test_kwargs(self):
        """ """
        h = self.value()
        copy = h.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is h)

    def test_kwargs_int(self):
        """ """
        h = self.value()
        copy = h.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        h = self.value()
        h.save()
        key = self.name + "." + h.id
        with open('file.json', 'r') as fi:
            g = json.load(fi)
            self.assertEqual(g[key], h.to_dict())

    def test_str(self):
        """ """
        h = self.value()
        self.assertEqual(str(h), '[{}] ({}) {}'.format(self.name, h.id,
                         h.__dict__))

    def test_todict(self):
        """ """
        h = self.value()
        m = h.to_dict()
        self.assertEqual(h.to_dict(), m)

    def test_kwargs_none(self):
        """ """
        m = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**m)

    def test_kwargs_one(self):
        """ """
        m = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**m)

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
        m = new.to_dict()
        new = BaseModel(**m)
        self.assertFalse(new.created_at == new.updated_at)
