from services.movie_service import MovieService
from src.movie import Movie


def test_add_movie():

    service = MovieService()

    movie = Movie("1", "Inception", "Sci-Fi")

    service.add_movie(movie)

    result = service.get_movie("1")

    assert result.title == "Inception"


def test_checkout_movie():

    service = MovieService()

    movie = Movie("2", "Avatar", "Action")

    service.add_movie(movie)

    service.checkout_movie("2")

    result = service.get_movie("2")

    assert result.status == "Checked Out"