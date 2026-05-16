from repositories.inmemory.inmemory_movie_repository import InMemoryMovieRepository


class MovieService:

    def __init__(self):
        self.repo = InMemoryMovieRepository()

    def add_movie(self, movie):
        self.repo.save(movie)
        return movie

    def get_movie(self, movie_id):
        return self.repo.find_by_id(movie_id)

    def get_all_movies(self):
        return self.repo.find_all()

    def delete_movie(self, movie_id):
        self.repo.delete(movie_id)

    def checkout_movie(self, movie_id):
        movie = self.repo.find_by_id(movie_id)

        if movie is None:
            raise Exception("Movie not found")

        movie.status = "Checked Out"

        self.repo.save(movie)

        return movie