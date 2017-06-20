from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=35)

class Movie(models.Model):
    name = models.CharField(max_length=140)
    year = models.PositiveSmallIntegerField()
    genre = models.ForeignKey(Genre)
