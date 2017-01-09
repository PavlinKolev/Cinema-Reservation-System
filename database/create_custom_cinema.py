import os
from database.cinema_db import CinemaDB
from decorators.atomic import atomic


@atomic
def set_data(db):
    db.cinema.add_movie("Transporter", 10.0)  # 1
    db.cinema.add_movie("Game of Thrones", 9.5)  # 2
    db.cinema.add_movie("Hunger Games", 7.5)  # 3
    db.cinema.add_movie("Transformers", 7.5)  # 4
    db.cinema.add_movie("Inferno", 6.9)  # 5

    db.cinema.register_user("Rosi", "Rosi123")  # 1
    db.cinema.register_user("Pavkata", "Pavkata123")  # 2
    db.cinema.register_user("Marto", "Marto123")  # 3
    db.cinema.register_user("Pesho", "Pesho123")  # 4

    db.cinema.add_projection(1, "2D", "2016-12-18", "19:00")
    db.cinema.add_projection(1, "2D", "2016-12-18", "19:00")
    db.cinema.add_projection(1, "2D", "2016-12-18", "19:00")
    db.cinema.add_projection(2, "4DX", "2017-12-18", "19:00")
    db.cinema.add_projection(3, "2D", "2016-12-18", "19:00")
    db.cinema.add_projection(4, "3D", "2016-12-18", "19:00")
    db.cinema.add_projection(5, "3D", "2016-12-18", "19:00")
    db.cinema.add_projection(5, "4DX", "2017-12-18", "19:00")

    db.cinema.add_reservation(1, 1, 1, 1)
    db.cinema.add_reservation(1, 2, 9, 9)
    db.cinema.add_reservation(1, 3, 1, 5)
    db.cinema.add_reservation(1, 4, 1, 6)
    db.cinema.add_reservation(1, 5, 7, 1)
    db.cinema.add_reservation(1, 6, 7, 1)
    db.cinema.add_reservation(1, 1, 8, 1)
    db.cinema.add_reservation(1, 2, 9, 1)
    db.cinema.add_reservation(1, 3, 3, 5)
    db.cinema.add_reservation(1, 4, 1, 5)
    db.cinema.add_reservation(1, 5, 6, 5)


def is_cinema_existing(cinema_name):
    file_path = os.getcwd() + '/' + cinema_name + '.db'
    if os.path.isfile(file_path):
        return True
    return False
