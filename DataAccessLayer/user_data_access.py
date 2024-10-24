import sqlite3  # make a connection through database
from Common.Entites.user import User
from DataAccessLayer import database_name


class UserDataAccess:
    # if it has any common thing with other ayers it should have init, but it doesn't so , we don't have any init function
    def get_user_with_username_password(self, username, password):
        # we get username and password from business layer (outer space)
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""SELECT id,
                                     first_name,
                                     last_name,
                                     username,
                                     password,
                                     role_id,
                                     is_active
                              FROM User
                              WHERE username = ? AND password = ?
                           """, (username, password))

            # because we did fetchone the data type of the "data" is a tuple
            # we use fetchone : if there is only a unique answer like identity code
            # we use fetchall : if there are more than one answers like searching for a name
            data = cursor.fetchone()

            # we create an instant from the User class because we want to code in object-oriented form
            # instead of writing the data[0],... we could write : *data (unpacking) in the parentheses , but due to security presences
            # we don't want to show the password to others . therefore our implementation would be like below
            # User(data[0], data[1], data[2], data[3], None)
            # but if we wanted to write the code as unpacking form ot would be like this :
            if data:
                user = User(*data)
                user.password = None
                return user
            return None

    def get_user_by_username(self, username):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, first_name, last_name, username, password,role_id FROM User WHERE username = ?",
                           (username,))
            data = cursor.fetchone()
            if data:
                return User(*data)
            return None

    def create_user(self, user):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                   INSERT INTO User (
                    first_name,
                    last_name,
                    username,
                    password,
                    role_id,
                    is_active
                )
                    VALUES (?, ?, ?, ?, ?, ?)
            """, (user.firstname, user.lastname, user.username, user.password, 2, 0))
                connection.commit()
                return True
            except sqlite3.Error:
                return False

    # user-id is id of the person who has logged in
    # Reason : we need all the users except this person
    def get_user_list(self, user_id):
        user_list = []
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""SELECT id,
                                                 first_name,
                                                 last_name,
                                                 username,
                                                 password,
                                                 role_id,
                                                 is_active
                                          FROM User
                                          Where id != ?
                            """, (user_id,))  # don't forget this comma after this data structure
            data = cursor.fetchall()
            for item in data:
                # unpacking data
                user = User(*item)
                user.password = None  # we don't want that admin sees the password, so we change it to None
                user_list.append(user)

            return user_list

    def update_is_active(self, user_id, new_value):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""    UPDATE   User
                                        SET      is_active = ?
                                        WHERE    id  = ?  
            """, (new_value, user_id))

            connection.commit()
