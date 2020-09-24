from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("detail", args=(self.pk,))


class BookImage(models.Model):
    url = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_image = models.ManyToManyField(BookImage)
