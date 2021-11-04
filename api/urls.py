from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', BookViewSet, basename='books')
urlpatterns = router.urls