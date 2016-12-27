import sqlite3
from queries import *
from password import encode
from validators import validate_movie_rating, validate_movie_type, validate_movie_date, validate_movie_time, validate_password, validate_row_col


class CinemaDB:
    def __init__(self, cinema_name):
        self.db = sqlite3.connect(cinema_name)
        self.cursor = db.cursor()
        self.__create_movies_table()
        self.__create_projections_table()
        self.__create_users_table()
        self.__create_reservations_table()

    def __create_movies_table(self):
        self.cursor.execute(CREATE_MOVIES_TABLE)
        self.__set_movies_ids()
        self.db.commit()

    def __create_projections_table(self):
        self.cursor.execute(CREATE_PROJECTIONS_TABLE)
        self.__set_projections_ids()
        self.db.commit()

    def __create_users_table(self):
        self.cursor.execute(CREATE_USERS_TABLE)
        self.__set_users_ids()
        self.db.commit()

    def __create_reservations_table(self):
        self.cursor.execute(CREATE_RESERVATIONS_TABLE)
        self.__set_reservations_ids()
        self.db.commit()

    def __set_movies_ids(self):
        self.cursor.execute(LIST_MOVIES_IDS)
        movies = self.cursor.fetchall()
        self.movies_ids = [m['ID'] for m in movies]

    def __set_projections_ids(self):
        self.cursor.execute(LIST_ROJECTIONS_IDS)
        projections = self.cursor.fetchall()
        self.projections_ids = [pr['ID'] for pr in projections]

    def __set_users_ids(self):
        self.cursor.execute(LIST_USERS_IDS)
        users = self.cursor.fetchall()
        self.users_ids = [u['ID'] for u in users]

    def __set_reservations_ids(self):
        self.cursor.execute(LIST_RESERVATIONS_IDS)
        reservations = self.cursor.fetchall()
        self.reservations_ids = [r['ID'] for r in reservations]

    def add_movie(self, name, rating):
        validate_movie_rating(rating)
        self.cursor.execute(ADD_MOVIE, (name, rating))

    def add_projection(self, movie_id, movie_type, movie_date, movie_time):
        self.__validate_movie_id(movie_id)
        validate_movie_type(movie_type)
        validate_movie_date(movie_date)
        validate_movie_time(movie_time)
        self.cursor.execute(ADD_PROJECTION, (movie_id, movie_type, movie_date, movie_time))
        self.db.commit()

    def add_user(self, username, password):
        validate_password(password)
        self.cursor.execute(ADD_USER, (username, encode(password)))
        self.db.commit()

    def add_reservation(self, user_id, projection_id, row, col):
        self.__validate_user_id(user_id)
        self.__validate_projection_id(projection_id)
        self.__validate_row_col_projection(row, col)
        self.cursor.execute(add_reservation, (user_id, projection_id, row, col))

    def __validate_row_col_projection(self, projection_id, row, col):
        validate_row_col(row, col)
        self.cursor.execute(SEATS_FOR_PROJECTION, (projection_id, ))
        if (row, col) in [(r['ROW'], r['COL']) for r in self.cursor.fetchall()]:
            raise ValueError("This seat is already taken")

    def __validate_movie_id(self, movie_id):
        if movie_id not in self.movies_ids:
            raise ValueError("There is no movie with this id.")

    def __validate_user_id(self, user_id):
        if user_id not in self.users_ids:
            raise ValueError("There is no user with this id.")

    def __validate_projection_id(self, projection_id):
        if projection_id not in self.projections_ids:
            raise ValueError("There is no projection with this id.")

    def __validate_reservation_id(self, reservation_id):
        if reservation_id not in self.reservations_ids:
            raise ValueError("There is no reservation with this id.")
