from tkinter import Frame, Label, Entry, Button, messagebox
from BusinessLayer.user_business_logic import UserBusinessLogic
from Common.Decorators.performance_logger import performance_logger_decorator


# Frame is its parent
class LoginFrame(Frame):
    # by giving it the window parameter we assign that this frame should be displayed on this form
    def __init__(self, window, main_view):
        super().__init__(window)

        self.main_view = main_view

        self.user_business_logic = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)
        # class object inside the class is "self" while outside the class we assign to a variable
        # Label() asked where should this Label be ? by giving itself as argument we say here in login frame
        self.title_Label = Label(self, text="Login Form")
        self.title_Label.grid(row=0, column=1, pady=10, sticky="w")

        self.username_Label = Label(self, text="Username")
        self.username_Label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_Label = Label(self, text="Password")
        self.password_Label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.login_button = Button(self, text="Login", command=self.login)
        self.login_button.grid(row=3, column=1, pady=(0, 10), sticky="w")

        self.register_button = Button(self, text="Register",command=self.open_register_frame)
        self.register_button.grid(row=4, column=1, pady=(0, 10), sticky="w")

    @performance_logger_decorator("LoginFrame")
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # result is an object from response class
        result = self.user_business_logic.login(username, password)

        if result.success:
            # messagebox.showinfo("Information",f"Welcome {result.data.get_fullname()}")
            home_frame = self.main_view.switch_frame("home")
            home_frame.set_current_user(result.data)

            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")

        else:
            messagebox.showerror("Error", result.message)

    @performance_logger_decorator("LoginFrame")
    def open_register_frame(self):
        self.main_view.switch_frame("register")
