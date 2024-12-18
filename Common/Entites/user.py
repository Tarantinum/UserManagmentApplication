# this file is consists of the user entities .
#Software entities are basically the building blocks of a software program :Classes,Objects,Functions/Methods,Variables,Modules
from Common.Entites.user_enum import UserRole
class User:
    # This method must have a value for all the columns in the database table
    def __init__(self, id, firstname, lastname, username, password, role_id, is_active):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.role_id = role_id
        # 0 >> False , 1 >> True
        self.is_active = bool(is_active)

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def show_role_title(self):
        match self.role_id:
            case 1:
                return "Admin"
            case 2:
                return "Default User"
            case _:
                raise ValueError("Invalid value for Role_Id")



    # def show_role_title(self):
    #     match self.role_id:
    #         case UserRole.ADMIN.value:
    #             return "Admin"
    #         case UserRole.DEFAULT_USER.value:
    #             return "Default User"
    #         case _:
    #             return None
