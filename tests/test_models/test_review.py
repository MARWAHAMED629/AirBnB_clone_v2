#!/usr/bin/python3
"""
Test module for the Review model.
"""  # Descriptive module docstring

from tests.test_models.test_base_model import test_basemodel  # Import statement
from models.review import Review  # Import statement


class test_Review(test_basemodel):
    """
    Tests for the Review class.
    """  # Class docstring

    def __init__(self, *args, **kwargs):
        """
        Initializes the test class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"  # Set class name
        self.value = Review  # Set class under test

    def test_place_id(self):
        """
        Tests the place_id attribute's type.
        """
        new = self.value()  # Create a new Review instance
        self.assertEqual(type(new.place_id), str)  # Assert attribute type

    def test_user_id(self):
        """
        Tests the user_id attribute's type.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)  # Assert attribute type

    def test_text(self):
        """
        Tests the text attribute's type.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)  # Assert attribute type
