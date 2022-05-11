from rest_framework import serializers
from BookManager.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('bookId', 'bookName', 'bookAuthor')
