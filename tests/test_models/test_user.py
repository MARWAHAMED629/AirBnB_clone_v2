#!/usr/bin/python3
"""
Test module for the User model.
"""  # Descriptive module docstring

from tests.test_models.test_base_model import test_basemodel  # Import statement
from models.user import User  # Import statement


class test_User(test_basemodel):
    """
    Tests for the User class.
    """  # Class docstring

    def __init__(self, *args, **kwargs):
        """
        Initializes the test class.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"  # Set class name
        self.value = User  # Set class under test

    def test_first_name(self):
        """
        Tests the first_name attribute's type.
        """
        new = self.value()  # Create a new User instance
        self.assertEqual(type(new.first_name), str)  # Assert first_name is a string

    def test_last_name(self):
        """
        Tests the last_name attribute's type.
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)  # Assert last_name is a string

    def test_email(self):
        """
        Tests the email attribute's type.
        """
        new = self.value()
        self.assertEqual(type(new.email), str)  # Assert email is a string

    def test_password(self):
        """
        Tests the password attribute's type.
        """
        new = self.value()
        self.assertEqual(type(new.password), str)  # Assert password is a string
