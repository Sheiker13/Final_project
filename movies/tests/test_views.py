
from django.test import TestCase, Client
from django.urls import reverse
from movies.models import Movie

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(
            title="View Movie",
            description="Some desc",
            release_date="2022-01-01"
        )

    def test_catalog_view(self):
        response = self.client.get(reverse("movie_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)

    def test_movie_detail_view(self):
        response = self.client.get(reverse("movie_detail", kwargs={"pk": self.movie.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)
