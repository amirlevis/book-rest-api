from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication

from .models import Book, Author, Illustrator
from .serailzers import BookSerializer, AuthorSerializer, IllustratorSerializer
from .policies import BookAccessPolicy


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (BookAccessPolicy,)

    #def create(self, request, *args, **kwargs):


class AuthorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = (TokenAuthentication,)


class IllustratorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage Illustrators in Database"""

    queryset = Illustrator.objects.all()
    serializer_class = IllustratorSerializer
    authentication_classes = (TokenAuthentication,)
