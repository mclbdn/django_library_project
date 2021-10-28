from django.urls import path
from .views import HomeView, BookListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all-books/', BookListView.as_view(), name='all-books'),
]