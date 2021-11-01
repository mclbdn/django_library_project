from django.test import TestCase
from django.urls import reverse
from .models import Book

# Book model tests


class BookTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="My Test Title",
            year=1960,
            page_count=211,
            author="F. Scott Fitzgerald",
        )

    def test_string_representation(self):
        self.assertEqual(str(self.book), "My Test Title")

    def test_book_content(self):
        self.assertEqual(self.book.title, "My Test Title")
        self.assertEqual(self.book.year, 1960)
        self.assertEqual(self.book.page_count, 211)
        self.assertEqual(self.book.author, "F. Scott Fitzgerald")


# Views tests


class HomePageViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")


class AllBooksViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/all-books/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("all-books"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("all-books"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "book_list.html")


class AddBookViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/add-book/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("add-book"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("add-book"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "add_book.html")


class SearchAndDeleteBookViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/search-book/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("search-book"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("search-book"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "search_book.html")


class ResultsViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/results/", {"q": "harry"})
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("results"), {"q": "harry"})

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("results"), {"q": "harry"})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "results.html")
