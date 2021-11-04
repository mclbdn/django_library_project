from rest_framework import serializers
from library import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'year', 'page_count')
        model = models.Book