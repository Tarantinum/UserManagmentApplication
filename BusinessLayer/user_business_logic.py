# all the businesses that are realated to the user should be implemented in here
from Common.ResponseModels.response import Response
from DataAccessLayer.user_data_access import UserDataAccess
from Common.Entites.user import User
import hashlib


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def login(self, username, password):
        if len(username) < 3 or len(password) < 3:
            return Response(False, "invalid request", None)

        password_hash = hashlib.md5(password.encode()).hexdigest()

        user = self.user_data_access.get_user_with_username_password(username, password_hash)
        if not user:
            return Response(False, " Invalid username or password . ", None)
        else:
            if user.is_active:
                return Response(True, None, user)
            else:
                return Response(False, "Your account is inactive", None)

    def register(self, firstname, lastname, username, password):
        if not all([firstname, lastname, username, password]):
            return Response(False, "All fields are required", None)

        existing_user = self.user_data_access.get_user_by_username(username)
        if existing_user:
            return Response(False, "Username already exists", None)

        password_hash = hashlib.md5(password.encode()).hexdigest()
        new_user = User(None, firstname, lastname, username, password_hash,2,0)
        success = self.user_data_access.create_user(new_user)

        if success:
            return Response(True, "Registration successful.", None)
        else:
            return Response(False, "Registration failed", None)

    # we first do some examinations before going through data
    def get_user_list(self, current_user):
        if not current_user.is_active:
            return Response(False, "Your account is Inactive ", None)

        if not current_user.show_role_title() == "Admin":
            return Response(False, " Access Denied ", None)

        # now it's time for picking data, but we are not connected to the db, so first we should get connected
        # we send a request to data access layer

        user_list = self.user_data_access.get_user_list(current_user.id)
        return Response(True, None, user_list)

    def active_user(self, current_user, user_list):
        # it gets the current user again in order to make sure the admin is already active
        if not current_user.is_active:
            return Response(False, "Your account is Inactive ", None)

        if not current_user.show_role_title() == "Admin":
            return Response(False, " Access Denied ", None)

        for user_id in user_list:
            self.user_data_access.update_is_active(user_id, 1)

    def user_inactive(self, current_user, user_list):
        # it gets the current user again in order to make sure the admin is already active
        if not current_user.is_active:
            return Response(False, "Your account is Inactive ", None)

        if not current_user.show_role_title() == "Admin":
            return Response(False, " Access Denied ", None)

        for user_id in user_list:
            self.user_data_access.update_is_active(user_id, 0)
