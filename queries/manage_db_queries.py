UPDATE_USER_IS_ACTIVE = '''
    UPDATE USERS
    SET IS_ACTIVE = ?
    WHERE ID = ?
'''

MAKE_ALL_USERS_NOT_LOGGED_OUT = '''
    UPDATE USERS
    SET IS_ACTIVE=0
'''

LIST_MOVIES_ORDERED_BY_RATING = '''
    SELECT ID, NAME, RATING
    FROM MOVIES
    ORDER BY RATING
'''

MOVIE_PROJECTIONS = '''
    SELECT PR.ID, MOVIES.NAME, PR.TYPE, PR.DATE, PR.TIME
    FROM MOVIES
    LEFT JOIN PROJECTIONS AS PR ON MOVIES.ID == PR.MOVIE_ID
    WHERE MOVIES.ID == ?
'''

MOVIE_PROJECTIONS_ORDERED_BY_DATE = '''
    SELECT PR.ID, MOVIES.NAME, PR.TYPE, PR.DATE, PR.TIME , ? - COUNT(RS.ID)
    FROM MOVIES
    JOIN PROJECTIONS AS PR ON MOVIES.ID == PR.MOVIE_ID
    LEFT JOIN RESERVATIONS AS RS ON RS.PROJECTION_ID == PR.ID
    GROUP BY PR.ID
    HAVING MOVIES.ID == ?
    ORDER BY DATE;
'''

MOVIE_PROJECTIONS_FOR_DATE = '''
    SELECT PR.ID, MOVIES.NAME, PR.TYPE, PR.DATE, PR.TIME , ? - COUNT(RS.ID)
    FROM MOVIES
    JOIN PROJECTIONS AS PR ON MOVIES.ID == PR.MOVIE_ID
    LEFT JOIN RESERVATIONS AS RS ON RS.PROJECTION_ID == PR.ID
    GROUP BY PR.ID
    HAVING MOVIES.ID == ? AND PR.DATE == ?
'''

COUNT_UNAVAILABLE_SEATS_FOR_PROJECTION = '''
    SELECT COUNT(ID)
    FROM RESERVATIONS
    GROUP BY PROJECTION_ID
    HAVING PROJECTION_ID==?
'''

USERNAME_OF_USER = '''
    SELECT USERNAME
    FROM USERS
    WHERE ID == ?
'''

ID_OF_USER_BY_USERNAME = '''
    SELECT ID
    FROM USERS
    WHERE USERNAME==?
'''

PASSWORD_OF_USER = '''
    SELECT PASSWORD
    FROM USERS
    WHERE ID==?
'''

SEATS_FOR_PROJECTION = '''
    SELECT ROW, COL
    FROM RESERVATIONS
    WHERE PROJECTION_ID==?
'''

DETELE_RESERVATION = '''
    DELETE FROM RESERVATIONS
    WHERE ID==?
'''

DELETE_ALL_RESERVATION_OF_USER = '''
    DELETE FROM RESERVATIONS
    WHERE USER_ID==?
'''
