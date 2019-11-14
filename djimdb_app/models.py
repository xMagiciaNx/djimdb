from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=32)
    description = models.TextField(max_length=256)


class Rating(models.Model):
    def __str__(self):
        return f'{self.movie.title} by {self.user.username}'

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()

    class Meta:
        unique_together = ('movie', 'user')
