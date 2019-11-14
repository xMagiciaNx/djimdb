from django.contrib.auth.models import User
from rest_framework import serializers
from djimdb_app.models import Movie, Rating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','description','avgrating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','movie','user','stars')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')
