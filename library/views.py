from django.views.generic import TemplateView, CreateView, DeleteView
from django.views.generic.list import ListView
from library.forms import BookForm
from .forms import BookForm
from .models import Book
from .tables import BookTable
from django_tables2 import SingleTableView
from django.db.models import Q
from django.urls import reverse_lazy


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

class BookListView(SingleTableView):
    model = Book
    table_class = BookTable
    template_name = 'book_list.html'

class AddBookView(CreateView):
    template_name = "add_book.html"

    form_class = BookForm

class SearchBookView(TemplateView):
    template_name = "search_book.html"


class ResultsView(ListView):
    model = Book
    template_name = 'results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return object_list

class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy('all-books')