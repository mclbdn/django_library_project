from django.contrib import admin
from .models import Book

class HomeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'year', 'page_count', 'added')

# Register your models here.

admin.site.register(Book, HomeAdmin)