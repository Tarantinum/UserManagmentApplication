from tkinter import Tk
from unittest import TestCase
from unittest.mock import Mock
from PeresntationLayer.Frames.login import LoginFrame
from Common.Entites.user import User
from Common.ResponseModels.response import Response


class TestLoginFrame(TestCase):
    def setUp(self):
        self.root = Tk()
        self.mock_main_view = Mock()
        self.login_frame = LoginFrame(self.root, self.mock_main_view)

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

    def test_login_attempt_with_valid_credentials(self):
        # Set up test data
        test_username = "Mori123"
        test_password = "123456"
        test_user = User(1, "Morteza", "Raha", test_username, None, 1, True)

        # Mock the business logic response
        self.login_frame.user_business_logic.login = Mock(
            return_value=Response(True, None, test_user)
        )

        # Set entry values
        self.login_frame.username_entry.insert(0, test_username)
        self.login_frame.password_entry.insert(0, test_password)

        # Perform login
        self.login_frame.login()

        # Verify main_view.switch_frame was called with "home"
        self.mock_main_view.switch_frame.assert_called_with("home")

    def test_login_attempt_with_invalid_credentials(self):
        # Set up test data
        test_username = "invalid"
        test_password = "wrong"

        # Mock the business logic response
        self.login_frame.user_business_logic.login = Mock(
            return_value=Response(False, "Invalid username or password", None)
        )

        # Set entry values
        self.login_frame.username_entry.insert(0, test_username)
        self.login_frame.password_entry.insert(0, test_password)

        # Perform login
        self.login_frame.login()

        # Verify main_view.switch_frame was NOT called
        self.mock_main_view.switch_frame.assert_not_called()

    def tearDown(self):
        self.root.destroy()
