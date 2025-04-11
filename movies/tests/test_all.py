
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from movies.models import Movie, Genre, CustomUser, Review, Rating
from datetime import date

@pytest.mark.django_db
def test_movie_creation():
    genre = Genre.objects.create(name="Action")
    movie = Movie.objects.create(title="Test Movie", description="Desc", release_date=date.today())
    movie.genres.add(genre)
    assert movie.title == "Test Movie"
    assert genre in movie.genres.all()

@pytest.mark.django_db
def test_user_registration(client):
    response = client.post("/accounts/register/", {
        "username": "testuser",
        "email": "testuser@example.com",
        "password1": "strongpass123",
        "password2": "strongpass123"
    })
    assert response.status_code in (200, 302)
    assert CustomUser.objects.filter(username="testuser").exists()

@pytest.mark.django_db
def test_api_movies_list():
    client = APIClient()
    Movie.objects.create(title="API Movie", description="Desc", release_date=date.today())
    url = reverse("movie-list")
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()["results"][0]["title"] == "API Movie"

@pytest.mark.django_db
def test_api_review_crud():
    client = APIClient()
    user = CustomUser.objects.create_user(username="apiuser", password="pass1234")
    movie = Movie.objects.create(title="M1", description="D", release_date=date.today())
    client.force_authenticate(user=user)
    review_data = {"user": user.id, "movie": movie.id, "text": "Nice!"}
    response = client.post(reverse("review-list"), data=review_data)
    assert response.status_code == 201
    assert Review.objects.filter(movie=movie, user=user).exists()
