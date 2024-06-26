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
        self.clase = 'BaseModel'
        self.value = BaseModel
        self.base = self.value()
        self.name = "Basecita"

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
        i = self.base
        self.assertEqual(type(i), BaseModel)

    def test_kwargs(self):
        """ """
        i = self.base
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.base
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db',
                     "Using filestorage")
    def test_save(self):
        """ Testing save """
        i = self.base
        i.save()
        key = self.clase + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.base
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.clase, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.base
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertEqual(new.Name, 'test')

    def test_id(self):
        """ """
        new = self.base
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.base
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.base
        initial_updated_at = new.updated_at
    # Make a change to the object
        new.some_attribute = "some_value"
    # Save the object to trigger the update of updated_at
        new.save()
    # Retrieve the object again
        updated_object = BaseModel(**new.to_dict())
        self.assertNotEqual(updated_object.updated_at, initial_updated_at)
