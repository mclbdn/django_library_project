from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    added = models.DateTimeField(auto_now=True)
    page_count = models.IntegerField()
    author = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('all-books')