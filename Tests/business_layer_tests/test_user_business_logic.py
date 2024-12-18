from unittest import TestCase
from unittest.mock import Mock
from BusinessLayer.user_business_logic import UserBusinessLogic
from Common.Entites.user import User
from Common.ResponseModels.response import Response


class TestUserBusinessLogic(TestCase):
    def setUp(self):
        self.user_business = UserBusinessLogic()
        self.user_business.user_data_access = Mock()

        # Create test users
        self.admin_user = User(1, "Admin", "User", "admin", None, 1, True)
        self.regular_user = User(2, "Regular", "User", "regular", None, 2, True)
        self.inactive_user = User(3, "Inactive", "User", "inactive", None, 2, False)

        # Create PerformanceLogger table
        import sqlite3
        with sqlite3.connect("UserManagmentNew.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS PerformanceLogger (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    function_name TEXT,
                    executation_time REAL,
                    call_datetime TEXT
                )
            """)

    def test_login_valid_credentials(self):
        # Setup
        username = "testuser"
        password = "testpass"
        test_user = User(1, "Test", "User", username, None, 2, True)
        self.user_business.user_data_access.get_user_with_username_password.return_value = test_user

        # Execute
        result = self.user_business.login(username, password)

        # Verify
        self.assertTrue(result.success)
        self.assertEqual(result.data, test_user)

    def test_login_invalid_credentials(self):
        # Setup
        self.user_business.user_data_access.get_user_with_username_password.return_value = None

        # Execute
        result = self.user_business.login("wrong", "wrong")

        # Verify
        self.assertFalse(result.success)
        self.assertEqual(result.message, " Invalid username or password . ")

    def test_register_success(self):
        # Setup
        self.user_business.user_data_access.get_user_by_username.return_value = None
        self.user_business.user_data_access.create_user.return_value = True

        # Execute
        result = self.user_business.register("Test", "User", "testuser", "password")

        # Verify
        self.assertTrue(result.success)
        self.assertEqual(result.message, "Registration successful.")

    def test_get_user_list_admin_access(self):
        # Setup
        test_users = [self.regular_user, self.inactive_user]
        self.user_business.user_data_access.get_user_list.return_value = test_users

        # Execute
        result = self.user_business.get_user_list(self.admin_user)

        # Verify
        self.assertTrue(result.success)
        self.assertEqual(result.data, test_users)

    def test_active_user_success(self):
        # Setup
        user_ids = [2, 3]

        # Execute
        result = self.user_business.active_user(self.admin_user, user_ids)

        # Verify
        self.user_business.user_data_access.update_is_active.assert_called()

    def test_inactive_user_success(self):
        # Setup
        user_ids = [2, 3]

        # Execute
        result = self.user_business.user_inactive(self.admin_user, user_ids)

        # Verify
        self.user_business.user_data_access.update_is_active.assert_called()
