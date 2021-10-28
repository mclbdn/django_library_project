from django.views.generic import TemplateView, ListView, CreateView

from library.forms import BookForm

from .models import Book

from .forms import BookForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

class BookListView(ListView):
    template_name = 'book_list.html'

    model = Book

    context_object_name = 'books'

class AddBookView(CreateView):
    template_name = "add_book.html"

    form_class = BookForm