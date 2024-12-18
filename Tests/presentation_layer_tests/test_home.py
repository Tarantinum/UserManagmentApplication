from tkinter import Tk
from unittest import TestCase
from unittest.mock import Mock
from PeresntationLayer.Frames.home import HomeFrame
from Common.Entites.user import User


class TestHomeFrame(TestCase):
    def setUp(self):
        self.root = Tk()
        self.mock_main_view = Mock()
        self.home_frame = HomeFrame(self.root, self.mock_main_view)

    def test_set_current_user_with_admin(self):
        admin_user = User(1, "Morteza", "Raha", "Mori123", None, 1, True)
        self.home_frame.set_current_user(admin_user)
        self.assertTrue(hasattr(self.home_frame, 'user_management_button'))

    def test_set_current_user_with_regular_user(self):
        regular_user = User(2, "Jana", "Samami", "jana123", None, 2, True)
        self.home_frame.set_current_user(regular_user)
        self.assertFalse(hasattr(self.home_frame, 'user_management_button'))

    def test_welcome_message_display(self):
        user = User(1, "Test", "User", "testuser", None, 2, True)
        self.home_frame.set_current_user(user)
        expected_message = f"Welcome {user.get_fullname()}"
        actual_message = self.home_frame.welcome_label.cget("text")
        self.assertEqual(expected_message, actual_message)

    def test_user_management_button_command(self):
        admin_user = User(1, "Admin", "User", "adminuser", None, 1, True)
        self.home_frame.set_current_user(admin_user)
        # Compare the function references directly
        self.assertIs(self.home_frame.user_management_button['command'].__func__,
                      HomeFrame.go_to_user_management)

    def tearDown(self):
        self.root.destroy()
