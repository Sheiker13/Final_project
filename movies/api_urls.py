<<<<<<< HEAD
from django.urls import path
from rest_framework.routers import DefaultRouter

# from .api_views import MovieViewSet

# router = DefaultRouter()
# router.register(r'movies', MovieViewSet)

urlpatterns = [
    # path('example/', SomeAPIView.as_view())
]

# urlpatterns += router.urls
=======

from rest_framework.routers import DefaultRouter
from .api_views import MovieViewSet, ReviewViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = router.urls
>>>>>>> e25a141 (Улучшил интерфейс)
