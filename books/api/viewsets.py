from rest_framework import viewsets
from books.api import serializers
from rest_framework import generics
from books.models import (
    Books,
)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = Books.objects.all()


class CreateBookView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = serializers.BooksSerializer
