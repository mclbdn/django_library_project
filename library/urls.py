from django.urls import path
from .views import HomeView, BookListView, AddBookView, SearchBookView, ResultsView, DeleteBookView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all-books/', BookListView.as_view(), name='all-books'),
    path('add-book/', AddBookView.as_view(), name='add-book'),
    path('search-book/', SearchBookView.as_view(), name='search-book'),
    path('results/', ResultsView.as_view(), name='results'),
    path('delete-book/<int:pk>/', DeleteBookView.as_view(), name='delete-book')
]