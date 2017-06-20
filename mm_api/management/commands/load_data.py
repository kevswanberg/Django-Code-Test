from django.core.management.base import BaseCommand

from mm_api.models import Movie, Genre


class Command(BaseCommand):
    """
    Save everything in movews_genres.tsv to a database
    """

    def handle(self, *args, **options):
        genres = {}
        movies = []
        Movie.objects.all().delete()
        Genre.objects.all().delete()

        with open('files/movies_genres.tsv', 'r') as movie_file:
            for line in movie_file:
                name, year, genre_name = line.strip().split('\t')
                genre = genres.get(genre_name)
                if genre is None:
                    genre = Genre.objects.create(name=genre_name)
                    genres[genre_name] = genre
                movies.append(Movie(name=name, year=year, genre=genre))
            Movie.objects.bulk_create(movies)
        print('Loaded {} movies'.format(Movie.objects.all().count()))
        print('Loaded {} genres'.format(Genre.objects.all().count()))
