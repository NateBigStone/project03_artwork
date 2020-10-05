import unittest
from unittest.mock import patch
from peewee import *
from main import *
from ui import *

"""
python3.8 -m unittest tests/test_main.py
http://docs.peewee-orm.com/en/latest/peewee/database.html#testing-peewee-applications
"""

MODELS = [Artist, Artwork]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')


class TestMain(unittest.TestCase):

    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)
        generate_test_tables()

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

    """
    Get Action
    Should mock the menu class
    """
    def test_get_action(self):
        test_menu = create_menu()
        self.assertEqual(test_menu.get_action('1'), add_artist)

    """Creates a New Artist"""
    @patch('ui.input', return_value='Unit Test')
    def test_add_artist(self, input):
        self.assertRaises(Exception, add_artist())

    """Search All Art"""
    def test_search_artist_all(self):
        self.assertEqual(True, True)

    """Search Available Art"""
    def test_search_artist_available(self):
        self.assertEqual(True, True)

    """Add Artwork"""
    def test_add_artwork(self):
        self.assertEqual(True, True)

    """Delete Artwork"""
    def test_delete_artwork(self):
        self.assertEqual(True, True)

    """Change Artwork availability"""
    def test_availability_artwork(self):
        self.assertEqual(True, True)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

        # If we wanted, we could re-bind the models to their original
        # database here. But for tests this is probably not necessary.
