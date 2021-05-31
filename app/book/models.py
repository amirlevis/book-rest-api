from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Illustrator(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    name = models.CharField(max_length=255)
    alias_name = models.CharField(max_length=255, blank=True)
    pages = models.PositiveSmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    illustrator = models.ForeignKey(Illustrator, on_delete=models.CASCADE)
    # icon = models.ImageField()
    description = models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
