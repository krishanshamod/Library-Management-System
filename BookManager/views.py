from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BookManager.models import Book
from BookManager.serializers import BookSerializer


@csrf_exempt
def add_book(request):
    book_data = JSONParser().parse(request)
    book_serializer = BookSerializer(data=book_data)

    if book_serializer.is_valid():
        book_serializer.save()
        return JsonResponse("Added Successfully", safe=False)

    return JsonResponse("Failed to add", safe=False)


@csrf_exempt
def get_books(request):
    books = Book.objects.all()
    book_serializer = BookSerializer(books, many=True)

    return JsonResponse(book_serializer.data, safe=False)
