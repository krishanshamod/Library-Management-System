from django.urls import path
from . import views

urlpatterns = [
    path('addbook/', views.add_book),
    path('getbooks/', views.get_books)
]
