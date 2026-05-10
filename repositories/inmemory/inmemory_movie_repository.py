from repositories.movie_repository import MovieRepository

class InMemoryMovieRepository(MovieRepository):

    def __init__(self):
        self._storage = {}

    def save(self, movie):
        self._storage[movie.movie_id] = movie

    def find_by_id(self, movie_id):
        return self._storage.get(movie_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, movie_id):
        if movie_id in self._storage:
            del self._storage[movie_id]