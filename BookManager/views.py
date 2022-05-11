from django.http import HttpResponse


def add_book(request):
    return HttpResponse("Added the book")
