from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, IllustratorViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('illustrators', IllustratorViewSet)

app_name = 'book'

urlpatterns = [
    path('', include(router.urls))
]
