import getpass
from validators import validate_password


class UserInterface:
    def choose_user(self):
        if self.user_id is None:
            self.user_id = self.log_or_sign()
        else:
            self.user_id = self.change_user(self.user_id)

    def log_or_sign(self):
        print("1) Log in as existing user\n" +
                "2) Register as new user")
        choose = input(":> ")
        if choose == "1":
            return self.__log_user()
        elif choose == "2":
            return self.__register_user()
        else:
            raise ValueError("Wrong input.")

    def change_user(self, user_id):
        username = self.cinema.get_username_for_id(user_id)
        print("You are logged as: " + username)
        print("1) Stay with this user\n" +
                "2) Login or register")
        choose = input(":> ")
        if choose == "1":
            return user_id
        elif choose == "2":
            self.cinema.log_out_user(user_id)
            return self.log_or_sign()
        else:
            raise ValueError("Wrong input.")

    def __register_user(self):
        username = self.__read_new_username()
        password = self.__read_new_user_password()
        return self.cinema.register_user(username, password)

    def __log_user(self):
        user_id = self.__read_username()
        self.__read_existing_user_password(user_id)
        return user_id

    def __read_username(self):
        while True:
            try:
                username = input("username:> ")
                user_id = self.cinema.get_id_of_username(username)
                return user_id
            except ValueError as error:
                input(str(error) + "\nPress Enter to continue...")

    def __read_existing_user_password(self, user_id):
        while True:
            try:
                password = getpass.getpass("password:> ")
                self.cinema.validate_password_of_user(user_id, password)
                break
            except ValueError as error:
                input(str(error) + "\nPress Enter to continue...")

    def __read_new_username(self):
        while True:
            try:
                username = input("username:> ")
                self.cinema.validate_new_username(username)
                return username
            except ValueError as error:
                input(str(error) + "\nPress Enter to continue...")

    def __read_new_user_password(self):
        while True:
            try:
                password = getpass.getpass("password:> ")
                validate_password(password)
                pass_2 = getpass.getpass("password:> ")
                if password != pass_2:
                    raise ValueError("Different password.")
                return password
            except ValueError as error:
                input(str(error) + "\nPress Enter to continue...")

    def cancel_reservation(self, user_name):
        self.cinema.remove_reservations_for_user(user_name)
