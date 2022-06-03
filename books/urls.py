from django.urls import path
from books.api.viewsets import (
    CreateBookView,
)

urlpatterns = [
    path('createBooks/', CreateBookView.as_view(), name='create-book'),
]
