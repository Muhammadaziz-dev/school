# yourapp/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Book

class SearchAPITest(TestCase):
    def setUp(self):
        # Create some test data
        Book.objects.create(name="Book1", id=1, slug="book-1")
        Book.objects.create(name="Book2", id=2, slug="book-2")
        Book.objects.create(name="AnotherBook", id=3, slug="another-book")

    def test_search_api(self):
        client = APIClient()

        # Case 1: No search query
        response = client.get(reverse('city-search-api'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)  # Assuming 3 books in the database

        # Case 2: Search for "Book1"
        response = client.get(reverse('city-search-api'), {'query': 'Book1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Book1')

        # Case 3: Search for "NonexistentBook"
        response = client.get(reverse('city-search-api'), {'query': 'NonexistentBook'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
