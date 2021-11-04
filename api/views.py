from rest_framework import viewsets
from library import models
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer