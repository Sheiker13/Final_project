
import pytest
from movies.models import CustomUser, Movie, Rating
from django.db.utils import IntegrityError

@pytest.mark.django_db
def test_create_rating():
    user = CustomUser.objects.create_user(username='rater', password='123')
    movie = Movie.objects.create(title='Rating Movie', description='...', release_date='2024-01-01')
    rating = Rating.objects.create(user=user, movie=movie, score=8)
    assert rating.score == 8
    assert Rating.objects.count() == 1

@pytest.mark.django_db
def test_unique_user_movie_rating():
    user = CustomUser.objects.create_user(username='rater2', password='123')
    movie = Movie.objects.create(title='Unique Movie', description='...', release_date='2024-01-01')
    Rating.objects.create(user=user, movie=movie, score=7)
    with pytest.raises(IntegrityError):
        Rating.objects.create(user=user, movie=movie, score=6)
