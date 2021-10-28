from django.views.generic import TemplateView, CreateView
from library.forms import BookForm
from .forms import BookForm
from .models import Book
from .tables import BookTable
from django_tables2 import SingleTableView


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