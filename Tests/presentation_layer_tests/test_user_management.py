from tkinter import Tk
from unittest import TestCase
from unittest.mock import Mock
from PeresntationLayer.Frames.user_managment import UserManagementFrame
from Common.Entites.user import User
from Common.ResponseModels.response import Response


class TestUserManagementFrame(TestCase):
    def setUp(self):
        # Create test users first
        self.admin_user = User(1, "Admin", "User", "admin", None, 1, True)
        self.test_users = [
            User(2, "Test1", "User1", "test1", None, 2, True),
            User(3, "Test2", "User2", "test2", None, 2, False)
        ]

        # Then initialize Tk and frame
        self.root = Tk()
        self.user_management_frame = UserManagementFrame(self.root)

        # Mock get_user_list
        self.user_management_frame.user_business.get_user_list = Mock(
            return_value=Response(True, None, self.test_users)
        )

    def test_set_current_user_loads_data(self):
        # Mock business logic response
        self.user_management_frame.user_business.get_user_list = Mock(
            return_value=Response(True, None, self.test_users)
        )

        # Set current user
        self.user_management_frame.set_current_user(self.admin_user)

        # Verify data was loaded into treeview
        items = self.user_management_frame.user_treeview.get_children()
        self.assertEqual(len(items), len(self.test_users))

    def test_active_button(self):
        # Setup test data
        self.user_management_frame.user_business.active_user = Mock(
            return_value=Response(True, None, None)
        )
        self.user_management_frame.current_user = self.admin_user

        # Simulate selection
        self.user_management_frame.user_treeview.selection = Mock(return_value=[2, 3])

        # Trigger active
        self.user_management_frame.active()

        # Verify business logic was called
        self.user_management_frame.user_business.active_user.assert_called_once()

    def test_inactive_button(self):
        # Setup test data
        self.user_management_frame.user_business.user_inactive = Mock(
            return_value=Response(True, None, None)
        )
        self.user_management_frame.current_user = self.admin_user

        # Simulate selection
        self.user_management_frame.user_treeview.selection = Mock(return_value=[2, 3])

        # Trigger inactive
        self.user_management_frame.inactive()

        # Verify business logic was called
        self.user_management_frame.user_business.user_inactive.assert_called_once()

    def tearDown(self):
        self.root.destroy()
