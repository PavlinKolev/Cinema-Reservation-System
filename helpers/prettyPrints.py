from prettytable import PrettyTable
from helpers.color_print import print


def prettyPrintMovies(movies):
    table = PrettyTable()
    table.field_names = ["Id", "Name", "Rating"]
    for m in movies:
        table.add_row(m)
    print(table)


def prettyPrintMovieProjections(projections):
    table = PrettyTable()
    table.field_names = ["Id", "Movie", "Type", "Date", "Time", "Free seats"]
    for pr in projections:
        table.add_row(pr)
    print(table)


def print_matrix_hall(matrix):
    table = PrettyTable()
    table.field_names = ["-"] + list(range(1, len(matrix) + 1))
    i = 1
    for line in matrix:
        table.add_row([i] + line)
        i += 1
    print(table)
