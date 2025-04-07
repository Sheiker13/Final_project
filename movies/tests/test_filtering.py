import pytest
from movies.models import Movie

@pytest.mark.django_db
def test_movie_creation_and_query():
    Movie.objects.create(title='Film A', description='desc', release_date='2023-01-01')
    Movie.objects.create(title='Film B', description='desc', release_date='2022-01-01')
    movies = Movie.objects.filter(title__icontains='Film')
    assert movies.count() == 2