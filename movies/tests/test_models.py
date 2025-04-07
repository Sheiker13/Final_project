import pytest
from movies.models import Movie

@pytest.mark.django_db
def test_movie_str():
    movie = Movie.objects.create(
        title="Inception",
        description="A dream within a dream",
        release_date="2010-07-16"
    )
    assert str(movie) == "Inception"
