from django.views.generic import TemplateView, ListView

from .models import Book

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