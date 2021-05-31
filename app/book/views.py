from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import Book
from .serailzers import *


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
