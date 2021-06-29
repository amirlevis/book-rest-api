from django.contrib import admin

from .models import Book, Author, Illustrator

admin.site.register((Book, Author, Illustrator))
