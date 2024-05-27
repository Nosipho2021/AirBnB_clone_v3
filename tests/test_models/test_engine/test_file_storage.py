#!/usr/bin/python3
"""
Unit tests for FileStorage class.
"""

import unittest
from models import storage
from models.user import User

class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage.
    """
    def setUp(self):
        """
        Set up test variables and initialize the app.
        """
        self.user = User(email="test@example.com", password="testpass")
        storage.new(self.user)
        storage.save()

    def tearDown(self):
        """
        Clean up after each test.
        """
        storage.delete(self.user)
        storage.save()

    def test_get(self):
        """
        Test retrieving an object by class and ID.
        """
        user = storage.get(User, self.user.id)
        self.assertEqual(user.id, self.user.id)

    def test_get_nonexistent(self):
        """
        Test retrieving a non-existent object.
        """
        user = storage.get(User, "nonexistent_id")
        self.assertIsNone(user)

    def test_count(self):
        """
        Test counting the number of objects in storage.
        """
        count = storage.count(User)
        self.assertEqual(count, 1)

    def test_count_all(self):
        """
        Test counting all objects in storage.
        """
        count = storage.count()
        self.assertGreaterEqual(count, 1)

if __name__ == "__main__":
    unittest.main()

