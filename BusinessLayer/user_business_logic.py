# all the businesses that are realated to the user should be implemented in here
from Common.Decorators.performance_logger import performance_logger_decorator
from Common.ResponseModels.response import Response
from DataAccessLayer.user_data_access import UserDataAccess
from Common.Entites.user import User
import hashlib
from BusinessLayer.jwt_service import generate_token
import jwt
from BusinessLayer.jwt_service import decode_token

class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    @performance_logger_decorator("UserBusinessLogic")
    def login(self, username, password):
        if len(username) < 3 or len(password) < 3:
            return Response(False, "invalid request", None)
        password_hash = hashlib.md5(password.encode()).hexdigest()
        user = self.user_data_access.get_user_with_username_password(username, password_hash)
        if not user:
            return Response(False, "Invalid username or password.", None)
        if not user.is_active:
            return Response(False, "Your account is inactive", None)

        # NEW: generate token and return it as the data payload
        token = generate_token(user)
        return Response(True, None, token)

    @performance_logger_decorator("UserBusinessLogic")
    def register(self, firstname, lastname, username, password):
        if not all([firstname, lastname, username, password]):
            return Response(False, "All fields are required", None)

        existing_user = self.user_data_access.get_user_by_username(username)
        if existing_user:
            return Response(False, "Username already exists", None)

        password_hash = hashlib.md5(password.encode()).hexdigest()
        new_user = User(None, firstname, lastname, username, password_hash, 2, 0)
        success = self.user_data_access.create_user(new_user)

        if success:
            return Response(True, "Registration successful.", None)
        else:
            return Response(False, "Registration failed", None)

    @performance_logger_decorator("UserBusinessLogic")
    def get_user_list(self, token):
        try:
            payload = decode_token(token)
        except jwt.ExpiredSignatureError:
            return Response(False, "Session expired. Please log in again.", None)
        except jwt.InvalidTokenError:
            return Response(False, "Invalid session. Please log in again.", None)

        if not payload["is_active"]:
            return Response(False, "Your account is Inactive", None)
        if payload["role_id"] != 1:
            return Response(False, "Access Denied", None)

        user_list = self.user_data_access.get_user_list(payload["user_id"])
        return Response(True, None, user_list)

    @performance_logger_decorator("UserBusinessLogic")
    def active_user(self, token, user_list):
        try:
            payload = decode_token(token)
        except jwt.ExpiredSignatureError:
            return Response(False, "Session expired. Please log in again.", None)
        except jwt.InvalidTokenError:
            return Response(False, "Invalid session. Please log in again.", None)

        if not payload["is_active"]:
            return Response(False, "Your account is Inactive", None)
        if payload["role_id"] != 1:
            return Response(False, "Access Denied", None)

        for user_id in user_list:
            self.user_data_access.update_is_active(user_id, 1)
        return Response(True, "Users activated successfully.", None)

    @performance_logger_decorator("UserBusinessLogic")
    def user_inactive(self, token, user_list):
        try:
            payload = decode_token(token)
        except jwt.ExpiredSignatureError:
            return Response(False, "Session expired. Please log in again.", None)
        except jwt.InvalidTokenError:
            return Response(False, "Invalid session. Please log in again.", None)

        if not payload["is_active"]:
            return Response(False, "Your account is Inactive", None)
        if payload["role_id"] != 1:
            return Response(False, "Access Denied", None)

        for user_id in user_list:
            self.user_data_access.update_is_active(user_id, 0)
        return Response(True, "Users deactivated successfully.", None)