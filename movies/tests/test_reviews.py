import pytest
from django.contrib.auth.models import User
from movies.models import Movie, Review

@pytest.mark.django_db
def test_create_review_directly():
    user = User.objects.create_user(username='reviewer', password='123')
    movie = Movie.objects.create(title='Test Movie', description='desc', release_date='2024-01-01')
    review = Review.objects.create(user=user, movie=movie, text='Nice!')
    assert review.text == 'Nice!'
    assert review.movie == movie