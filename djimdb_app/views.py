from django.shortcuts import render
from rest_framework import viewsets
from djimdb_app.models import Movie, Rating
from djimdb_app.serializers import MovieSerializer, RatingSerializer

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RatingViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer