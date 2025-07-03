from rest_framework import serializers
from .models import Author, BookImage
from catalog.models import Book



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email', 'dob']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    images = serializers.HyperlinkedRelatedField(
        view_name='book-images-detail',
        queryset=BookImage.objects.all(),
        many=True
    )
    class Meta:
        model = Book
        #fields = '__all__'
        fields = ['id', 'title', 'summary','images', 'author']

class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'summary', 'isbn']

class BookImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        book_id = self.context['book_id']
        return BookImage.objects.create(pk=book_id, **validated_data)

    class Meta:
        model = BookImage
        fields = ['id', 'image']

    #Serializer
    #id = serializers.IntegerField()
    #title = serializers.CharField(max_length=255)
    #summary = serializers.CharField(max_length=255)