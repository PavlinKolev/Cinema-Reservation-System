class ProjectionInterface:
    def show_movie_projections(self, arguments):
        arguments = arguments.split(' ')
        movie_id = int(arguments[0])
        if len(arguments) == 2:
            date = arguments[1]
            self.cinema.show_movie_projections_for_date(movie_id, date)
        else:
            self.cinema.show_movie_projections(movie_id)

    def choose_projection(self, movie_id):
        while True:
            try:
                self.show_movie_projections(movie_id)
                projection_id = int(input("projection id:> "))
                self.cinema.validate_projection_id(projection_id)
                return projection_id
            except ValueError as error:
                input(str(error) + "\nPress Enter to continue...")
