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

import pytest
from movies.models import Movie, CustomUser, Review, Rating
from django.utils import timezone

@pytest.mark.django_db
def test_review_str():
    user = CustomUser.objects.create_user(username="reviewer", password="testpass")
    movie = Movie.objects.create(title="Test Movie", description="desc", release_date="2020-01-01")
    review = Review.objects.create(user=user, movie=movie, text="Great movie!")
    assert "Review by reviewer" in str(review)

@pytest.mark.django_db
def test_rating_constraints():
    user = CustomUser.objects.create_user(username="rater", password="testpass")
    movie = Movie.objects.create(title="Rated Movie", description="desc", release_date="2020-01-01")
    rating = Rating.objects.create(user=user, movie=movie, score=8)
    assert rating.score == 8
    assert str(rating) == f"8 - {movie.title} by {user.username}"
