from tkinter import Frame, Label, Entry, Button, messagebox
from BusinessLayer.user_business_logic import UserBusinessLogic


class RegisterFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.main_view = main_view
        self.user_business_logic = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)

        self.firstname_label = Label(self, text="First Name")
        self.firstname_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.lastname_label = Label(self, text="Last Name")
        self.lastname_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="e")

        self.password_entry = Entry(self)
        self.password_entry.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.repeat_password_label = Label(self, text=" Repeat your Password")
        self.repeat_password_label.grid(row=5, column=0, pady=(0, 10), padx=10, sticky="e")

        self.repeat_password_entry = Entry(self)
        self.repeat_password_entry.grid(row=5, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.register_button = Button(self, text="Register", command=self.register)
        self.register_button.grid(row=6, column=0, pady=(10, 0), sticky="w")

    def register(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        repeat_password = self.repeat_password_entry.get()

        if password != repeat_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        result = self.user_business_logic.register(firstname, lastname, username, password)

        if result.success:
            messagebox.showinfo("Success", "Registration successful.Please Wait to be Activated by The Admin")
            self.back_to_login()
        else:
            messagebox.showerror("Error", result.message)

    def back_to_login(self):
        self.main_view.switch_frame("Login")
