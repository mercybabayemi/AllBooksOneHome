
from django.shortcuts import render
from rest_framework import status

from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view()
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def greet(request, name):
    return render(request, 'index1.html', {'name': name})