from django.urls import path
from .views import HomeView, BookListView, AddBookView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all-books/', BookListView.as_view(), name='all-books'),
    path("add-book/", AddBookView.as_view(), name='add-book')
]