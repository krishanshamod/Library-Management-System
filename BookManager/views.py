from django.http import HttpResponse
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

