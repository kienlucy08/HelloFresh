"""Tests for the database management python file"""
import os
import sqlite3
import unittest
import database_management


class TestDatabaseManagement(unittest.TestCase):

    def test_database_created(self):
        # Test that the function creates a database with the given name
        database_management.create_database('test_db')
        self.assertTrue(os.path.isfile('test_db'))

