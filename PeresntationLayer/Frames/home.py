from tkinter import Frame, Label, Button


class HomeFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.main_view = main_view
        self.current_user = None

        self.welcome_label = Label(self)
        self.welcome_label.grid(row=0, column=0, pady=10)

        self.logout_button = Button(self, text="Logout", command=self.logout)
        self.logout_button.grid(row=1, column=1, pady=(0, 10), padx=20, sticky="ew")

        # we create the button, but we show it to the user only if he is an admin
        # self.user_management_button = None

    # def set_current_user(self, current_user):
    #     self.current_user = current_user
    #     self.welcome_label.config(text=f"Welcome {current_user.get_fullname()}")
    #
    #     if current_user.show_role_title() == "Admin":
    #         self.user_management_button = Button(self, text="User Management", command=self.go_to_user_management)
    #         self.user_management_button.grid(row=2, column=1, pady=(0, 10), padx=20, sticky="ew")
    #     else:
    #         if self.user_management_button:
    #             self.user_management_button.destroy()
    #             delattr(self, 'user_management_button')

    def set_current_user(self, current_user):
        self.current_user = current_user
        self.welcome_label.config(text=f"Welcome {current_user.get_fullname()}")

        if current_user.show_role_title() == "Admin":
            self.user_management_button = Button(self, text="User Management", command=self.go_to_user_management)
            self.user_management_button.grid(row=2, column=1, pady=(0, 10), padx=20, sticky="ew")
        else:
            if hasattr(self,
                       'user_management_button'):  # This change prevents the AttributeError by first checking if the attribute exists before trying to access it. The hasattr() function is the proper way to check for attribute existence in Python.
                self.user_management_button.destroy()
                delattr(self, 'user_management_button')

    def go_to_user_management(self):
        user_management_frame = self.main_view.switch_frame("user_management")
        user_management_frame.set_current_user(self.current_user)

    def logout(self):
        self.main_view.switch_frame("Login")
