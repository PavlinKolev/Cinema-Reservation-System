import datetime
from settings import (MIN_MOVIE_RATING, MAX_MOVIE_RATING, MOVIE_TYPES,
                    MIN_PASS_LEN, HALL_ROWS, HALL_COLS, OCCUPIED_SEAT)


def validate_movie_rating(rating):
    if type(rating) is not float and type(rating) is not int:
        raise TypeError("Type of movie rating must be real number.")
    if rating < MIN_MOVIE_RATING or rating > MAX_MOVIE_RATING:
        raise ValueError("Movie rating is out of range.")


def validate_movie_type(movie_type):
    if type(movie_type) is not str:
        raise TypeError("Type of movie type must be string")
    if movie_type not in MOVIE_TYPES:
        raise ValueError("Type of movie must be one of {}.".format(' '.join(MOVIE_TYPES)))


def validate_movie_date(movie_date):
    if type(movie_date) is not str:
        raise TypeError("Type of movie date must be string")
    # TODO: with regular expression
    year = int(movie_date.split('-')[0])
    month = int(movie_date.split('-')[1])
    day = int(movie_date.split('-')[2])
    # will raise ValueError if something is out of range
    datetime.datetime(year=year, month=month, day=day)


def validate_movie_time(movie_time):
    try:
        hour = int(movie_time.split(':')[0])
        minutes = int(movie_time.split(':')[1])
        if hour < 0 or hour > 23 or minutes < 0 or minutes > 60:
            raise ValueError("Invalid movie time")
    except:
        raise ValueError("Invalid movie time")


def validate_password(password):
    if len(password) < MIN_PASS_LEN:
        raise ValueError("Length of password must be at least {} symbols".format(MIN_PASS_LEN))
    no_upper = True
    no_lower = True
    no_digit = True
    for letter in password:
        if letter.isupper():
            no_upper = False
        if letter.islower():
            no_lower = False
        if letter.isdigit():
            no_digit = False
    if no_upper:
        raise ValueError("Password must have capital letter.")
    if no_lower:
        raise ValueError("Password must have lower letter.")
    if no_digit:
        raise ValueError("Password must have digit.")


def validate_row_col(row, col):
    validate_row(row)
    validate_col(col)


def validate_row(row):
    if row < 1 or row > HALL_ROWS:
        raise ValueError("Row is out of range: [{}:{}]".format(1, HALL_ROWS))


def validate_col(col):
    if col < 1 or col > HALL_COLS:
        raise ValueError("Col is out of range: [{}:{}]".format(1, HALL_COLS))


def validate_row_col_in_matrix(matrix, row, col):
    try:
        row = int(row) - 1
        col = int(col) - 1
        if row < 0 or row >= 10 or col < 0 or col >= 10:
            print("Row or col is out of range.")
            return False
    except ValueError:
        print("Type of row or col is not int.")
        return False
    if matrix[row][col] == OCCUPIED_SEAT:
        print("This seat is alredy taken! Please choose another seat.")
        return False
    return True
