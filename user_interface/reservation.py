from helpers.prettyPrints import print_matrix_hall
from helpers.clean_screen import clean_screen
from settings.general_settings import OCCUPIED_SEAT
from user_interface.validators import validate_row_col_in_matrix
from user_interface.user import UserInterface
from decorators.atomic import atomic
from decorators.user_exists import user_exists


class ReservationInterface:
    @user_exists
    def make_reservation(self, user_id):
        tickets = self.__read_number_of_tickets()
        movie_id = self.choose_movie()
        projection_id = self.choose_projection(movie_id)
        tickets = self.validate_tickets_for_projection(projection_id, tickets)
        matrix = self.cinema.matrix_seats_for_projection(projection_id)
        seats = self.__choose_the_seats(tickets, matrix, projection_id)
        self.finalize(user_id, projection_id, seats)

    def validate_tickets_for_projection(self, projection_id, tickets):
        while True:
            try:
                self.cinema.validate_tickets_for_projection(projection_id, tickets)
                return tickets
            except ValueError as error:
                print(error)
                tickets = self.__read_number_of_tickets()

    def __read_number_of_tickets(self):
        while True:
            try:
                tickets = int(input("number of tickets:> "))
                if tickets < 1 or tickets > 100:
                    raise ValueError("Unvalid number of tickets")
                return tickets
            except ValueError as error:
                print(error)

    def __choose_the_seats(self, tickets, matrix, projection_id):
        seats = []
        for i in range(tickets):
            while True:
                clean_screen()
                print_matrix_hall(matrix)
                row = input("row:> ")
                col = input("col:> ")
                try:
                    validate_row_col_in_matrix(matrix, row, col)
                    matrix[int(row) - 1][int(col) - 1] = OCCUPIED_SEAT
                    seats.append([int(row), int(col)])
                    break
                except ValueError as error:
                    print(error)
        return seats

    @atomic
    def finalize(self, user_id, projection_id, seats):
        for [r, c] in seats:
            self.cinema.add_reservation(user_id, projection_id, r, c)
        print("Your reservation is saved. Happy Cinema!")
