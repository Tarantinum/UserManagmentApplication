from tkinter import Frame, Label, Button
import jwt
from BusinessLayer.jwt_service import decode_token, get_role_title

class HomeFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.main_view = main_view
        self.current_token = None           # stores token string (was current_user)
        self.user_management_button = None  # track the button so we can show/hide it

        self.welcome_label = Label(self)
        self.welcome_label.grid(row=0, column=0, pady=10)

        self.logout_button = Button(self, text="Logout", command=self.logout)
        self.logout_button.grid(row=1, column=1, pady=(0, 10), padx=20, sticky="ew")

    def set_current_user(self, token):
        self.current_token = token
        self._refresh_ui_for_role()

    def _refresh_ui_for_role(self):
        try:
            payload = decode_token(self.current_token)

            # Update welcome label using data from token
            fullname = payload["username"]  # or use firstname+lastname if you add them to token
            self.welcome_label.config(text=f"Welcome {fullname}")

            # Show user management button only for admins
            if payload["role_id"] == 1:
                if not self.user_management_button:
                    self.user_management_button = Button(
                        self,
                        text="User Management",
                        command=self.go_to_user_management
                    )
                    self.user_management_button.grid(row=2, column=1, pady=(0, 10), padx=20, sticky="ew")
            else:
                # Not an admin — remove the button if it exists
                if self.user_management_button:
                    self.user_management_button.destroy()
                    self.user_management_button = None

        except jwt.ExpiredSignatureError:
            from tkinter import messagebox
            messagebox.showerror("Session Expired", "Your session has expired. Please log in again.")
            self.main_view.switch_frame("login")

        except jwt.InvalidTokenError:
            from tkinter import messagebox
            messagebox.showerror("Error", "Invalid session. Please log in again.")
            self.main_view.switch_frame("login")

    def go_to_user_management(self):
        user_management_frame = self.main_view.switch_frame("user_management")
        user_management_frame.set_current_user(self.current_token)  # pass token, not user

    def logout(self):
        self.current_token = None           # clear the token on logout
        self.main_view.switch_frame("login")