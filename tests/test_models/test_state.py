#!/usr/bin/python3
"""
Test module for the State model.
"""  # Descriptive module docstring

from tests.test_models.test_base_model import test_basemodel  # Import statement
from models.state import State  # Import statement


class test_State(test_basemodel):
    """
    Tests for the State class.
    """  # Class docstring

    def __init__(self, *args, **kwargs):
        """
        Initializes the test class.
        """
        super().__init__(*args, **kwargs)
        self.name = "State"  # Set class name
        self.value = State  # Set class under test

    def test_name(self):
        """
        Tests the name attribute's type.
        """
        new = self.value()  # Create a new State instance
        self.assertEqual(type(new.name), str)  # Assert name is a string
