from rest_framework import serializers
from user.models import Author
from catalog.models import Book



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    class Meta:
        model = Book
        #fields = '__all__'
        fields = ['id', 'title', 'summary', 'author']



    #Serializer
    #id = serializers.IntegerField()
    #title = serializers.CharField(max_length=255)
    #summary = serializers.CharField(max_length=255)