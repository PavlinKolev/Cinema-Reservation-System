import os
import sys
import getpass
from cinema_db import CinemaDB
from create_custom_cinema import set_data, is_cinema_existing
from validators import validate_password
from settings import SPELLS_COUNT, SPELLS


def validate_row_col_in_matrix(matrix, row, col):
    occupied = '■'
    try:
        row = int(row) - 1
        col = int(col) - 1
        if row < 0 or row >= 10 or col < 0 or col >= 10:
            return False
    except ValueError:
        return False
    if matrix[row][col] == occupied:
        print("This seat is alredy taken! Please choose another seat.")
        return False
    matrix[row][col] = occupied
    return True


def print_matrix(matrix):
    print("   1 2 3 4 5 6 7 8 9 10")
    i = 1
    for line in matrix:
        print("{:2} {}".format(i,  ' '.join(line)))
        i += 1


class Interface:
    def __init__(self, cinema_name):
        cinema_name = cinema_name.replace(' ', '-')
        db_was_not_existing = not(is_cinema_existing(cinema_name))
        self.cinema = CinemaDB(cinema_name + '.db')
        self.user_id = None
        # only if there was no database with this name, we populate it with data
        if db_was_not_existing:
            set_data(self.cinema)

    def run(self):
        while True:
            command = input(":> ")
            try:
                self.dispatch(command)
            except ValueError as error:
                input(str(error) + "\nPress Enter to continue...")

    def show_movies(self):
        self.cinema.show_movies()

    def show_movie_projections(self, arguments):
        arguments = arguments.split(' ')
        if len(arguments) == 2:
            movie_id = int(arguments[0])
            date = arguments[1]
            self.cinema.show_movie_projections_for_date(movie_id, date)
        else:
            movie_id = int(arguments[0])
            self.cinema.show_movie_projections(movie_id)

    def make_reservation(self):
        if self.user_id is None:
            self.user_id = self.log_or_sign()
        tickets = int(input("number of tickets:> "))
        if tickets < 1 or tickets > 100:
            raise ValueError("Unvalid number of tickets")
        self.show_movies()
        movie_id = input("movie id:> ")
        self.cinema.validate_movie_id(int(movie_id))
        self.show_movie_projections(movie_id)
        projection_id = int(input("projection id:> "))
        self.cinema.validate_projection_id(projection_id)
        self.cinema.validate_free_seats_for_projection(projection_id, tickets)
        matrix = self.cinema.print_seats_for_projection(projection_id)
        for i in range(tickets):
            while True:
                print_matrix(matrix)
                row = input("row:> ")
                col = input("col:> ")
                if validate_row_col_in_matrix(matrix, row, col):
                    self.cinema.add_reservation(self.user_id, projection_id, int(row), int(col))
                    break

    def register_user(self):
        username = input("username:> ")
        password = getpass.getpass("password:> ")
        validate_password(password)
        pass_2 = getpass.getpass("password:> ")
        if password != pass_2:
            raise ValueError("Different password.")
        return self.cinema.register_user(username, password)

    def log_or_sign(self):
        print("1) Log in as existing user\n" +
                "2) Register as new user")
        choose = input(":> ")
        if choose == "1":
            return self.log_user()
        elif choose == "2":
            return self.register_user()
        else:
            raise ValueError("Wrong input.")

    def log_user(self):
        username = input("username:> ")
        password = getpass.getpass("password:> ")
        return self.cinema.login_user(username, password)

    def cancel_reservation(self, user_name):
        self.cinema.remove_reservations_for_user(user_name)

    def exit(self):
        sys.exit()

    def help(self):
        for i in range(SPELLS_COUNT):
            print("{}) {}".format(i + 1, SPELLS[i + 1]))

    def dispatch(self, command):
        if command == "show movies":
            self.show_movies()
        elif command == "make reservation":
            self.make_reservation()
        elif command.startswith("show movie projections"):
            self.show_movie_projections(command.split("show_movie_projections ")[1])
        elif command.startswith("cancel reservation"):
            self.cancel_reservation(command.split("cancel_reservation ")[1])
        elif command == "exit":
            self.exit()
        elif command == "help":
            self.help()
        else:
            raise ValueError("Wrong command.")
