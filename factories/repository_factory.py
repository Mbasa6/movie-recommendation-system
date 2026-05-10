from repositories.inmemory.inmemory_movie_repository import InMemoryMovieRepository
from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository


class RepositoryFactory:

    @staticmethod
    def get_movie_repository():
        return InMemoryMovieRepository()

    @staticmethod
    def get_user_repository():
        return InMemoryUserRepository()