from unittest import TestCase
import sqlite3
import os
from DataAccessLayer.user_data_access import UserDataAccess
from Common.Entites.user import User


class TestUserDataAccess(TestCase):
    @classmethod
    def setUpClass(cls):
        # Set test database path
        cls.test_db = "UserManagmentTest.db"

        # Override database name globally
        import DataAccessLayer.user_data_access as user_data_access
        user_data_access.database_name = cls.test_db

        # Create fresh database
        with sqlite3.connect(cls.test_db) as connection:
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS User")
            cursor.execute("""
                CREATE TABLE User (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    role_id INTEGER NOT NULL,
                    is_active INTEGER NOT NULL DEFAULT 0
                )
            """)
            connection.commit()

    def setUp(self):
        self.user_data_access = UserDataAccess()
        # Reset test data
        with sqlite3.connect(self.test_db) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM User")
            cursor.execute("""
                INSERT INTO User (first_name, last_name, username, password, role_id, is_active)
                VALUES 
                ('Test', 'Admin', 'admin', '123456', 1, 1),
                ('Test', 'User', 'testuser', '123456', 2, 1),
                ('Inactive', 'User', 'inactive', '123456', 2, 0)
            """)
            connection.commit()

    def test_get_user_with_username_password(self):
        user = self.user_data_access.get_user_with_username_password('admin', '123456')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'admin')
        self.assertIsNone(user.password)

    def test_get_user_by_username(self):
        user = self.user_data_access.get_user_by_username('testuser')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')

    def test_create_user(self):
        new_user = User(None, 'New', 'User', 'newuser', '123456', 2, 0)
        result = self.user_data_access.create_user(new_user)
        self.assertTrue(result)
        created_user = self.user_data_access.get_user_by_username('newuser')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.username, 'newuser')

    def test_get_user_list(self):
        users = self.user_data_access.get_user_list(1)
        self.assertEqual(len(users), 3)
        for user in users:
            self.assertIsNone(user.password)
            self.assertNotEqual(user.id, 1)

    def test_update_is_active(self):
        # First get the user's ID
        with sqlite3.connect(self.test_db) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM User WHERE username = ?", ('testuser',))
            user_id = cursor.fetchone()[0]

        # Update user status
        self.user_data_access.update_is_active(user_id, 0)

        # Verify the update
        with sqlite3.connect(self.test_db) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT is_active FROM User WHERE id = ?", (user_id,))
            updated_status = cursor.fetchone()[0]

        self.assertEqual(updated_status, 0)

    def tearDown(self):
        # Clean up after each test
        with sqlite3.connect(self.test_db) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM User")
            connection.commit()

    @classmethod
    def tearDownClass(cls):
        # Clean up the test database
        try:
            os.remove(cls.test_db)
        except:
            pass
