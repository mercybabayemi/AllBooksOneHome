import uuid

from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from user.models import Author

# Create your models here.

class Genre(models.Model):
    GENRE_CHOICES = (
        ("R", "Romance"),
        ("D", "Dance"),
        ("F", "Fantasy"),
        ("H", "History")
    )
    name = models.CharField(max_length=1, choices=GENRE_CHOICES, default="R", unique=True)
    def __str__(self):
        return self.name

class Language(models.Model):
    LANGUAGE_CHOICES = (
        ("en", "English"),
        ("fr", "French"),
        ("es", "Spanish"),
        ("Y", "Yoruba")
    )
    name = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default="en")
    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, related_name="books")
    summary = models.TextField()
    isbn = models.CharField(max_length=11, unique=True, validators=[])
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class BookInstance(models.Model):
    LOAN_STATUS = (
        ("A", "AVAILABLE"),
        ("B", "BORROWED"),
        ("M", "MAINTENANCE")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default="A", unique=True)
    return_date = models.DateField(blank=False, null=False)
    comments = models.TextField(blank=True, null=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title
