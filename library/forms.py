from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'year', 'page_count', 'author']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Book\'s title', 'style': 'max-width: 75%;'})
        self.fields['author'].widget.attrs.update({'placeholder': 'Author\'s full name', 'style': 'max-width: 75%;'})
        self.fields['year'].widget.attrs.update({'placeholder': 'Year this book was originally published', 'style': 'max-width: 50%;'})
        self.fields['page_count'].widget.attrs.update({'placeholder': 'Number of pages', 'style': 'max-width: 50%;'})