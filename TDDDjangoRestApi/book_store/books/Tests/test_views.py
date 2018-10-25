import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Book
from ..serializers import BookSerializer


# initialize the APIClient app
client = Client()


class GetAllBooksTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        Book.objects.create(
            title='The Hobbit', isbn='0618260307', author='J. R. R. Tolkien', num_pages=310, year_published=1937)
        Book.objects.create(
            title='Do Androids Dream of Electric Sheep?', isbn='9780345404473', author='Philip K. Dick', num_pages=210, year_published=1968)
        Book.objects.create(
            title='Neuromancer', isbn='9780441569595', author='William Gibson', num_pages=271, year_published=1984)
        Book.objects.create(
            title='Dune', isbn='9789896372484', author='Frank Herbert', num_pages=412, year_published=1965)
        Book.objects.create(
            title='Nineteen Eighty-Four', isbn='9780451524935', author='George Orwell', num_pages=328, year_published=1949)

    def test_get_all_books(self):
        # get API response
        response = client.get(reverse('get_post_books'))
        # get data from db
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
