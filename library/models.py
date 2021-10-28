from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    added = models.DateTimeField(auto_now=True)
    page_count = models.IntegerField()

    def __str__(self):
        return self.title