import sqlite3
from queries.create_db_queries import *
from queries.manage_db_queries import *
from helpers.password import encode
from helpers.prettyPrints import prettyPrintMovies, prettyPrintMovieProjections
from helpers.cinema_hall import cinema_hall_matrix
from settings.general_settings import MAX_SEATS
from user_interface.validators import (validate_movie_rating,
                                    validate_movie_type,
                                    validate_movie_date, validate_movie_time,
                                    validate_password, validate_row_col)


class CinemaDB:
    def __init__(self, cinema_name):
        self.db = sqlite3.connect(cinema_name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.__create_movies_table()
        self.__create_projections_table()
        self.__create_users_table()
        self.__create_reservations_table()

    def __del__(self):
        self.__close_data_base()

    # we want to close the database even if not handled exeption occurs
    def __exit__(Self, exc_type, exc_value, traceback):
        self.__close_data_base()

    def commit_to_database(self):
        self.db.commit()

    def roll_back(self):
        self.db.rollback()

    def __create_movies_table(self):
        self.cursor.execute(CREATE_MOVIES_TABLE)
        self.db.commit()

    def __create_projections_table(self):
        self.cursor.execute(CREATE_PROJECTIONS_TABLE)
        self.db.commit()

    def __create_users_table(self):
        self.cursor.execute(CREATE_USERS_TABLE)
        self.db.commit()

    def __create_reservations_table(self):
        self.cursor.execute(CREATE_RESERVATIONS_TABLE)
        self.db.commit()

    def add_movie(self, name, rating):
        validate_movie_rating(rating)
        self.cursor.execute(ADD_MOVIE, (name, rating))

    def add_projection(self, movie_id, movie_type, movie_date, movie_time):
        self.validate_movie_id(movie_id)
        validate_movie_type(movie_type)
        validate_movie_date(movie_date)
        validate_movie_time(movie_time)
        self.cursor.execute(ADD_PROJECTION, (movie_id, movie_type, movie_date, movie_time))

    def add_reservation(self, user_id, projection_id, row, col):
        self.validate_user_id(user_id)
        self.validate_projection_id(projection_id)
        self.__validate_row_col_projection(projection_id, row, col)
        self.cursor.execute(ADD_RESERVATION, (user_id, projection_id, row, col))

    def register_user(self, username, password):
        self.cursor.execute(ADD_USER, (username, encode(password)))
        self.db.commit()
        user_id = self.cursor.lastrowid
        self.__make_user_active(user_id)
        return user_id

    def log_out_user(self, user_id):
        self.cursor.execute(UPDATE_USER_IS_ACTIVE, (0, user_id))
        self.db.commit()

    def remove_reservations_for_user(self, user_name):
        user_id = self.get_id_of_username(user_name)
        self.cursor.execute(DELETE_ALL_RESERVATION_OF_USER, (user_id, ))
        self.db.commit()

    def get_username_for_id(self, user_id):
        self.validate_user_id(user_id)
        self.cursor.execute(USERNAME_OF_USER, (user_id, ))
        return self.cursor.fetchone()[0]

    def login_user(self, user_id):
        self.__make_user_active(user_id)

    def validate_new_username(self, username):
        self.cursor.execute(ID_OF_USER_BY_USERNAME, (username, ))
        result = self.cursor.fetchone()
        if result is not None:
            raise ValueError("This username is already taken.")

    def get_id_of_username(self, username):
        self.cursor.execute(ID_OF_USER_BY_USERNAME, (username, ))
        result = self.cursor.fetchone()
        if result is None:
            raise ValueError("No user wtih this username.")
        return result[0]

    def validate_password_of_user(self, user_id, password):
        self.cursor.execute(PASSWORD_OF_USER, (user_id, ))
        user_password = self.cursor.fetchone()[0]
        if encode(password) != user_password:
            raise ValueError("Wrong password for this username.")

    def __make_user_active(self, user_id):
        self.cursor.execute(UPDATE_USER_IS_ACTIVE, (1, user_id))
        self.db.commit()

    def matrix_seats_for_projection(self, projection_id):
        self.cursor.execute(SEATS_FOR_PROJECTION, (projection_id, ))
        return cinema_hall_matrix(self.cursor.fetchall())

    def validate_tickets_for_projection(self, projection_id, tickets):
        taken_seats = self.__count_of_taken_seats_for_projection(projection_id)
        free_seats = MAX_SEATS - taken_seats
        if free_seats < tickets:
            raise ValueError("Sorry but wannted tickets for this projection are too much.")

    def __count_of_taken_seats_for_projection(self, projection_id):
        self.cursor.execute(COUNT_UNAVAILABLE_SEATS_FOR_PROJECTION, (projection_id, ))
        result = self.cursor.fetchone()
        if result is None:
            return 0
        return result[0]

    def show_movie_projections_for_date(self, movie_id, date_):
        self.validate_movie_id(movie_id)
        self.cursor.execute(MOVIE_PROJECTIONS_FOR_DATE, (MAX_SEATS, movie_id, date_))
        prettyPrintMovieProjections(self.cursor.fetchall())

    def show_movie_projections(self, movie_id):
        self.validate_movie_id(movie_id)
        self.cursor.execute(MOVIE_PROJECTIONS_ORDERED_BY_DATE, (MAX_SEATS, movie_id))
        prettyPrintMovieProjections(self.cursor.fetchall())

    def show_movies(self):
        self.cursor.execute(LIST_MOVIES_ORDERED_BY_RATING)
        prettyPrintMovies(self.cursor.fetchall())

    def __validate_row_col_projection(self, projection_id, row, col):
        validate_row_col(row, col)
        self.cursor.execute(SEATS_FOR_PROJECTION, (projection_id, ))
        if (row, col) in [(r[0], r[1]) for r in self.cursor.fetchall()]:
            raise ValueError("This seat is already taken")

    def validate_movie_id(self, movie_id):
        self.cursor.execute(LIST_MOVIES_IDS)
        movies = self.cursor.fetchall()
        if movie_id not in [m[0] for m in movies]:
            raise ValueError("There is no movie with this id.")

    def validate_projection_id(self, projection_id):
        self.cursor.execute(LIST_ROJECTIONS_IDS)
        projections = self.cursor.fetchall()
        if projection_id not in [pr[0] for pr in projections]:
            raise ValueError("There is no projection with this id.")

    def validate_user_id(self, user_id):
        self.cursor.execute(LIST_USERS_IDS)
        users = self.cursor.fetchall()
        if user_id not in [u[0] for u in users]:
            raise ValueError("There is no user with this id.")

    def validate_reservation_id(self, reservation_id):
        self.cursor.execute(LIST_RESERVATIONS_IDS)
        reservations = self.cursor.fetchall()
        if reservation_id not in [r[0] for r in reservations]:
            raise ValueError("There is no reservation with this id.")

    def __close_data_base(self):
        self.cursor.execute(MAKE_ALL_USERS_NOT_LOGGED_OUT)
        self.db.commit()
        self.db.close()
