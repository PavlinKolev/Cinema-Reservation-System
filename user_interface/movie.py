from helpers.clean_screen import clean_screen
from decorators.atomic import atomic
from helpers.color_print import print, input_

class MovieInterface:
    @atomic
    def show_movies(self):
        self.cinema.show_movies()

    def choose_movie(self):
        while True:
            try:
                self.show_movies()
                movie_id = input_("movie id:> ")
                self.cinema.validate_movie_id(int(movie_id))
                return movie_id
            except ValueError as error:
                print(error)
