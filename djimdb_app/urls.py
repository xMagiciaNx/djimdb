from django.urls import path, include
from rest_framework import routers
from djimdb_app.views import MovieViewset, RatingViewset, UserViewset

router = routers.DefaultRouter()
router.register('movies',MovieViewset)
router.register('ratings',RatingViewset)
router.register('users',UserViewset)

urlpatterns = [
    path('', include(router.urls)),
]
