import datetime


def validate_movie_rating(rating):
    if type(rating) is not float:
        raise TypeError("Type of movie rating must be real number.")
    if rating < float(0) or rating > float(10):
        raise ValueError("Movie rating is out of range.")


def validate_movie_type(movie_type):
    if type(movie_type) is not str:
        raise TypeError("Type of movie type must be string")
    if movie_type != "2D" and movie_type != "3D" and movie_type != "4DX":
        raise ValueError("Type of movie must be 2D, 3D or 4DX")


def validate_movie_date(movie_date):
    if type(movie_date) is not str:
        raise TypeError("Type of movie date must be string")
    # TODO: with regular expression
    year = movie_date.split('-')[0]
    month = movie_date.split('-')[1]
    day = movie_date.split('-')[2]
    datetime.datetime(year=year, month=month, day=day)


def validate_movie_time(movie_time):
    try:
        hour = int(movie_time.split(':')[0])
        minutes = int(movie_time.split(':')[1])
        if hour < 0 or hour > 23 or minutes < 0 or minutes > 60:
            raise ValueError("Invalid movie time")
    except TypeError:
        raise ValueError("Invalid movie time")


def validate_password(password):
    if len(password) < 8:
        raise ValueError("Length of password must be at least {} symbols".format(8))
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
    if row < 1 or row > 10 or col < 1 or col > 10:
        raise ValueError("Row or col is out of range[1:10].")
