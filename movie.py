class MovieInterface:
    def show_movies(self):
        self.cinema.show_movies()

    def choose_movie(self):
        while True:
            try:
                self.show_movies()
                movie_id = input("movie id:> ")
                self.cinema.validate_movie_id(int(movie_id))
                return movie_id
            except ValueError as error:
                input(str(error) + "\nPress Enter to continue...")
