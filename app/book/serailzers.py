from rest_framework import serializers
from .models import Book, Author, Illustrator


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('id',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ('id',)


class IllustratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illustrator
        fields = '__all__'
        read_only_fields = ('id',)
