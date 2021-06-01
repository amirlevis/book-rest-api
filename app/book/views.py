from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, AllowAny
from rest_framework.response import Response
from .models import Book, Author, Illustrator
from .serailzers import BookSerializer, AuthorSerializer, IllustratorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes_by_action = {'list': [AllowAny], 'default': [IsAdminUser]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except:
            return [permission() for permission in self.permission_classes_by_action['default']]


class AuthorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage Authors in Database"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    permission_classes_by_action = {'list': [AllowAny], 'default': [IsAdminUser]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except:
            return [permission() for permission in self.permission_classes_by_action['default']]


class IllustratorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage Illustrators in Database"""

    queryset = Illustrator.objects.all()
    serializer_class = IllustratorSerializer

    permission_classes_by_action = {'list': [AllowAny], 'default': [IsAdminUser]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except:
            return [permission() for permission in self.permission_classes_by_action['default']]
