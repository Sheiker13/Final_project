from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Movie, Genre, Review, Rating

User = get_user_model()


class UserAuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_data = {
            "username": "testuser",
            "password": "testpass123"
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_login(self):
        response = self.client.post(reverse("login"), self.user_data)
        self.assertEqual(response.status_code, 302)

    def test_register(self):
        response = self.client.post(reverse("register"), {
            "username": "newuser",
            "password1": "newpass123",
            "password2": "newpass123"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())


class MovieModelTests(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Action")
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Just a test.",
            release_date="2020-01-01"
        )
        self.movie.genres.add(self.genre)

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Test Movie")

    def test_genre_str(self):
        self.assertEqual(str(self.genre), "Action")


class ReviewRatingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="reviewer", password="12345")
        self.movie = Movie.objects.create(
            title="Movie A",
            description="Description",
            release_date="2022-01-01"
        )

    def test_add_review(self):
        review = Review.objects.create(user=self.user, movie=self.movie, text="Great!")
        self.assertEqual(str(review), f"Review by {self.user.username} on {self.movie.title}")

    def test_add_rating(self):
        rating = Rating.objects.create(user=self.user, movie=self.movie, score=8)
        self.assertEqual(str(rating), f"{rating.score} - {self.movie.title} by {self.user.username}")