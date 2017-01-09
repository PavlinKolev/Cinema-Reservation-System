import os
import sys
from cinema_db import CinemaDB
from create_custom_cinema import set_data, is_cinema_existing
from settings import SPELLS_COUNT, SPELLS
from movie import MovieInterface
from projection import ProjectionInterface
from reservation import ReservationInterface
from user import UserInterface


class Interface(MovieInterface, ProjectionInterface,
                ReservationInterface, UserInterface):
    def __init__(self, cinema_name):
        cinema_name = cinema_name.replace(' ', '-')
        db_was_not_existing = not(is_cinema_existing(cinema_name))
        self.cinema = CinemaDB(cinema_name + '.db')
        self.user_id = None
        if db_was_not_existing:
            set_data(self.cinema)

    def run(self):
        while True:
            command = input(":> ")
            try:
                self.__dispatch(command)
            except ValueError as error:
                input(str(error) + "\nPress Enter to continue...")

    def __exit(self):
        sys.exit()

    def __help(self):
        for i in range(SPELLS_COUNT):
            print("-- {}".format(SPELLS[i + 1]))

    def __dispatch(self, command):
        if command == "show movies":
            self.show_movies()
        elif command == "make reservation":
            self.make_reservation()
        elif command.startswith("show movie projections"):
            arguments = command.split("show movie projections ")[1]
            self.show_movie_projections(arguments)
        elif command.startswith("cancel reservation"):
            arguments = command.split("cancel reservation ")[1]
            self.cancel_reservation(arguments)
        elif command == "exit":
            self.__exit()
        elif command == "help":
            self.__help()
        else:
            raise ValueError("Wrong command.")
