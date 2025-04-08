
import pytest
from movies.models import Movie

@pytest.mark.django_db
def test_movie_image_field():
    movie = Movie.objects.create(
        title='With Poster',
        description='With image',
        release_date='2024-01-01',
        image='movies/test.jpg'
    )
    assert movie.image.name == 'movies/test.jpg'
