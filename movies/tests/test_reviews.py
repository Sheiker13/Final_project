import pytest
from movies.models import CustomUser as User, Movie, Review


@pytest.mark.django_db
def test_create_review_directly():
    user = User.objects.create_user(username='reviewer', password='123')
    movie = Movie.objects.create(title='Test Movie', description='Test Description', release_date='2024-01-01')

    review = Review.objects.create(user=user, movie=movie, text='Great movie!')

    assert Review.objects.count() == 1
    assert review.user == user
    assert review.movie == movie
    assert review.text == 'Great movie!'
