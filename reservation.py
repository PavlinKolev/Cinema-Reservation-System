from prettyPrints import print_matrix_hall
from validators import validate_row_col_in_matrix
from settings import OCCUPIED_SEAT


class ReservationInterface:
    def make_reservation(self):
        self.choose_user()
        tickets = self.__read_number_of_tickets()
        movie_id = self.choose_movie()
        projection_id = self.choose_projection(movie_id)
        tickets = self.validate_tickets_for_projection(projection_id, tickets)
        matrix = self.cinema.matrix_seats_for_projection(projection_id)
        self.__choose_the_seats(tickets, matrix, projection_id)

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
                input(str(error) + "\nPress Enter to continue...")

    def __choose_the_seats(self, tickets, matrix, projection_id):
        for i in range(tickets):
            while True:
                print_matrix_hall(matrix)
                row = input("row:> ")
                col = input("col:> ")
                if validate_row_col_in_matrix(matrix, row, col):
                    matrix[int(row) - 1][int(col) - 1] = OCCUPIED_SEAT
                    self.cinema.add_reservation(self.user_id, projection_id, int(row), int(col))
                    break
                
