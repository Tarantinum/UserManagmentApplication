# BusinessLayer/jwt_service.py

import jwt
import datetime

SECRET_KEY = "university-project-secret-key-2024"
TOKEN_EXPIRY_MINUTES = 60


def generate_token(user: object) -> str:
    """Generate a signed JWT token from a User entity."""
    payload = {
        "user_id": user.id,
        "username": user.username,
        "role_id": user.role_id,
        "is_active": user.is_active,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRY_MINUTES)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_token(token: str) -> dict:
    """
    Decode and validate token.
    Raises jwt.ExpiredSignatureError if expired.
    Raises jwt.InvalidTokenError if tampered or invalid.
    """
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])


def get_role_title(token: str) -> str:
    """Returns 'Admin' or 'Default User' from the token payload."""
    payload = decode_token(token)
    match payload["role_id"]:
        case 1:
            return "Admin"
        case 2:
            return "Default User"
        case _:
            raise ValueError("Invalid role_id in token")