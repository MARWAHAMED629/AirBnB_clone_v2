#!/usr/bin/python3
""" Test module for the Place model."""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Tests for the Place class."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Tests the city_id attribute's type."""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Tests the user_id attribute's type. """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Tests the name attribute's type. """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Tests the description attribute's type. """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Tests the number_rooms attribute's type. """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Tests the number_rooms attribute's type. """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Tests the max_guest attribute's type. """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Tests the price_by_night attribute's type. """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Tests the latitude attribute's type. """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Tests the longitude attribute's type. """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Tests the amenity_ids attribute's type. """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
