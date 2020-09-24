from django.test import TestCase

# Create your tests here.
from main.models import Author, Book, BookImage

author = Author.objects.create(name="Ernest Hemingway")

with_image = Book.objects.create(title="The Old Man and the Sea", author=author)
no_image = Book.objects.create(title="A Farewell to Arms", author=author)

book_image = BookImage.objects.create(url="https://images-na.ssl-images-amazon.com/images/I/61Ar1qIRf8L.jpg")

with_image.book_image.add(book_image)

with_image.save()

