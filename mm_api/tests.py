from django.test import TestCase
from rest_framework.test import APIClient

from .models import Movie, Genre

class TestMovieViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.genre = Genre.objects.create(name='new genre')
        self.movie = Movie.objects.create(name='new movie', year=2017, genre=self.genre)
        Movie.objects.create(name='new movie 2', year=2017, genre=self.genre)

    def test_get_movies(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(
            response.json()['results'][0],
            {'id': self.movie.id, 'genre': 'new genre', 'name':'new movie', 'year': 2017, 'sequel_count': 1}
        )


class TestGenreViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.genre = Genre.objects.create(name='new genre')
        self.movie = Movie.objects.create(name='new movie', year=2017, genre=self.genre)

    def test_get_movies(self):
        response = self.client.get('/api/genres/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(
            response.json()['results'][0],
            {'id': self.genre.id, 'name': 'new genre', 'movie_count': 1}
        )
