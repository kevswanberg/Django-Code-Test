from rest_framework import serializers
from .models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    movie_count = serializers.ReadOnlyField()
    class Meta:
        fields = ('id', 'name', 'movie_count')
        model = Genre


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='name')

    sequel_count = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'name', 'genre', 'year', 'sequel_count')
        model = Movie

    def get_sequel_count (self, obj):
        return Movie.objects.filter(name__istartswith=obj.name).count() - 1
