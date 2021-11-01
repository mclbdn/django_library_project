from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomePageViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

class AllBooksViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/all-books/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('all-books'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('all-books'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'book_list.html')

class AddBookViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/add-book/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('add-book'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('add-book'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'add_book.html')

class SearchAndDeleteBookViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/search-book/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('search-book'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('search-book'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'search_book.html')

class ResultsViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/results/', {'q':'harry'})
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('results'), {'q':'harry'})

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('results'), {'q':'harry'})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'results.html')