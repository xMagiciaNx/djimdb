from django.contrib.auth.models import User
from rest_framework import viewsets, status, mixins
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from djimdb_app.models import Movie, Rating
from djimdb_app.serializers import MovieSerializer, RatingSerializer, UserSerializer, RatingUserSerializer


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        else:
            response = {'message':'you must be an admin'}
            return Response(response,status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().update(request, *args, **kwargs)
        else:
            response = {'message':'you must be an admin'}
            return Response(response,status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            response = {'message':'you must be an admin'}
            return Response(response,status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['POST'])
    def ratemovie(self, request, pk):
        if request.user.is_authenticated:
            if 'stars' in request.data:
                stars = request.data['stars']
                try:
                    if (stars < 1) or (stars > 5) or (isinstance(stars,float)):
                        raise Exception()
                except:
                    response = {'message': 'invalid integer'}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
                movie = Movie.objects.get(id=pk)
                user = request.user
                try:
                    rating = Rating.objects.get(user = user.id, movie = movie.id)
                    rating.stars = stars
                    rating.save()
                    response = {'message': 'success - updated'}
                except:
                    Rating.objects.create(user = user, movie = movie, stars = stars)
                    response = {'message':'success - created'}
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {'message': 'you must provide a star rating'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {'message': 'you must logged in to perform this action'}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class RatingViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return RatingSerializer
        return RatingUserSerializer

    def create(self, request, *args, **kwargs):
        response={'message':'You cannot edit rating directly'}
        return Response(response,status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        response={'message':'You cannot edit rating directly'}
        return Response(response,status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        response={'message':'You cannot edit rating directly'}
        return Response(response,status=status.HTTP_403_FORBIDDEN)

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )

    def create(self, request, *args, **kwargs):
        user = User.objects.create_user(request.data['username'],'',request.data['password'])
        Token.objects.create(user=user)
        response = {'message':f'User {user.username} created succesfull'}
        return Response(response,status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        response = {'message':f'not allowed to modify user'}
        return Response(response,status=status.HTTP_403_FORBIDDEN)