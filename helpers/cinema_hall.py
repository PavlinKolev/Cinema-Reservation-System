from settings.general_settings import FREE_SEAT, OCCUPIED_SEAT, HALL_COLS, HALL_ROWS


def cinema_hall_matrix(occ_seats):
    matrix = [[FREE_SEAT for j in range(HALL_COLS)] for i in range(HALL_ROWS)]
    for seat in occ_seats:
        matrix[seat[0] - 1][seat[1] - 1] = OCCUPIED_SEAT
    return matrix
