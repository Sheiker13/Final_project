from rest_framework.routers import DefaultRouter
from .api_views import MovieViewSet, ReviewViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = router.urls
