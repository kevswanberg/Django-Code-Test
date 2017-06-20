from django.db.models import Count, OuterRef, Subquery
from rest_framework import viewsets
from rest_framework.decorators import detail_route

from .models import Movie, Genre
from .serializers import GenreSerializer, MovieSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().annotate(movie_count=Count('movie')).order_by('-movie_count')
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.request.query_params.get('genre'):
            queryset = queryset.filter(genre__name=self.request.query_params.get('genre'))
        return queryset
