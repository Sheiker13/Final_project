
from django.test import TestCase
from django.urls import reverse
from .models import Movie, Genre, CustomUser

class MovieModelTest(TestCase):
    def test_movie_str(self):
        genre = Genre.objects.create(name="Action")
        movie = Movie.objects.create(title="Test Movie", description="Test", release_date="2024-01-01")
        movie.genres.add(genre)
        self.assertEqual(str(movie), "Test Movie")

class MovieListViewTest(TestCase):
    def test_movie_list_status(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
