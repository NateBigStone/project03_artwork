import unittest
from peewee import *
from main import *

"""
python3.8 -m unittest tests/test_main.py
"""

test_db = SqliteDatabase(':memory:')


class TestMain(unittest.TestCase):

    """Test Test"""
    def test_something(self):
        self.assertEqual(True, True)

    """Create Menu Function Returns a Menu Class"""
    def test_create_menu(self):
        self.assertIsInstance(create_menu(), Menu)

    """Valid Option"""
    def test_is_valid(self):
        test_menu = create_menu()
        self.assertTrue(test_menu.is_valid('1'))
        self.assertTrue(test_menu.is_valid('Q'))
        self.assertFalse(test_menu.is_valid(1))
        self.assertFalse(test_menu.is_valid('q'))
        self.assertFalse(test_menu.is_valid('sdlkjsldkjsljsdlskdjsdlgj'))

    """Creates a New Artist"""
    def test_add_artist(self):
        self.assertEqual(True, True)
