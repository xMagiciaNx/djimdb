from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    def __str__(self):
        return self.title

    def avgrating(self):
        sum = 0
        rating = Rating.objects.filter(movie = self)
        rateCount = len(rating)
        if rateCount > 0:
            for rate in rating:
                sum += rate.stars
            return sum/rateCount
        else:
            return 0

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
