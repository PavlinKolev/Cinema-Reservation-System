import os
from cinema_db import CinemaDB


def set_data(cinema):
    cinema.add_movie("Transporter", 10.0)  # 1
    cinema.add_movie("Game of Thrones", 9.5)  # 2
    cinema.add_movie("Hunger Games", 7.5)  # 3
    cinema.add_movie("Transformers", 7.5)  # 4
    cinema.add_movie("Inferno", 6.9)  # 5

    cinema.register_user("Rosi", "Rosi123")  # 1
    cinema.register_user("Pavkata", "Pavkata123")  # 2
    cinema.register_user("Marto", "Marto123")  # 3
    cinema.register_user("Pesho", "Pesho123")  # 4

    cinema.add_projection(1, "2D", "2016-12-18", "19:00")
    cinema.add_projection(1, "2D", "2016-12-18", "19:00")
    cinema.add_projection(1, "2D", "2016-12-18", "19:00")
    cinema.add_projection(2, "4DX", "2017-12-18", "19:00")
    cinema.add_projection(3, "2D", "2016-12-18", "19:00")
    cinema.add_projection(4, "3D", "2016-12-18", "19:00")
    cinema.add_projection(5, "3D", "2016-12-18", "19:00")
    cinema.add_projection(5, "4DX", "2017-12-18", "19:00")

    cinema.add_reservation(1, 1, 1, 1)
    cinema.add_reservation(1, 2, 9, 9)
    cinema.add_reservation(1, 3, 1, 5)
    cinema.add_reservation(1, 4, 1, 6)
    cinema.add_reservation(1, 5, 7, 1)
    cinema.add_reservation(1, 6, 7, 1)
    cinema.add_reservation(1, 1, 8, 1)
    cinema.add_reservation(1, 2, 9, 1)
    cinema.add_reservation(1, 3, 3, 5)
    cinema.add_reservation(1, 4, 1, 5)
    cinema.add_reservation(1, 5, 6, 5)


def is_cinema_existing(cinema_name):
    file_path = os.getcwd() + '/' + cinema_name + '.db'
    if os.path.isfile(file_path):
        return True
    return False
