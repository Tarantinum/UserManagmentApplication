from tkinter import Frame, Label, Button, messagebox
from tkinter.ttk import Treeview
from BusinessLayer.user_business_logic import UserBusinessLogic


class UserManagementFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.main_view = main_view  # ADD this
        self.row_list = []
        self.user_business = UserBusinessLogic()
        self.current_token = None  # was self.current_user
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.header_label = Label(self, text="User Management Form")
        self.header_label.grid(row=0, column=0, pady=10, padx=10)

        self.active_button = Button(self, text="Active", command=self.active)
        self.active_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.inactive_button = Button(self, text="Inactive", command=self.inactive)
        self.inactive_button.grid(row=1, column=1, pady=(0, 10), padx=10, sticky="e")

        self.user_treeview = Treeview(self, columns=("firstname", "lastname", "username", "role", "status"))
        self.user_treeview.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="nsew")

        self.user_treeview.heading("#0", text="NO")
        self.user_treeview.heading("#1", text="First Name")
        self.user_treeview.heading("#2", text="Last Name")
        self.user_treeview.heading("#3", text="Username")
        self.user_treeview.heading("#4", text="Role")
        self.user_treeview.heading("#5", text="Status")

    def set_current_user(self, token):  # receives token now, not a User object
        self.current_token = token
        self.get_user_list()

    def load_data(self, user_list):
        for row in self.row_list:
            self.user_treeview.delete(row)

        self.row_list.clear()

        row_number = 1
        for user in user_list:
            row = self.user_treeview.insert("", "end", iid=user.id, text=str(row_number),
                                            values=(user.firstname,
                                                    user.lastname,
                                                    user.username,
                                                    user.show_role_title(),
                                                    "Active" if user.is_active else "InActive"))
            self.row_list.append(row)
            row_number += 1

    def active(self):
        active_user_list = self.user_treeview.selection()
        result = self.user_business.active_user(self.current_token, active_user_list)
        if result and not result.success:
            messagebox.showerror("Error", result.message)
            return
        self.get_user_list()

    def inactive(self):
        inactive_user_list = self.user_treeview.selection()
        result = self.user_business.user_inactive(self.current_token, inactive_user_list)
        if result and not result.success:
            messagebox.showerror("Error", result.message)
            return
        self.get_user_list()

    def get_user_list(self):
        result = self.user_business.get_user_list(self.current_token)

        if result.success:
            self.load_data(result.data)
        else:
            messagebox.showerror("Error", result.message)
            if "expired" in result.message.lower() or "invalid session" in result.message.lower():
                self.main_view.switch_frame("Login")  # redirect to login
