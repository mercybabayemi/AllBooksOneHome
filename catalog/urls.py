from django.urls import path, include
from . import views
from .models import Author

from rest_framework_nested import routers

from .views import BookViewSet, BookImageViewSet

router = routers.DefaultRouter()
#router = routers.SimpleRouter()
router.register('books', BookViewSet, 'books')
router.register('images', BookImageViewSet, 'book-images')
print(router.urls)

book_image_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
book_image_router.register('images', BookImageViewSet, 'book-images')

urlpatterns = [
    # path("", views.get_books),
    #path("authors/", views.add_author, name="add_author"),
    path('', include(router.urls)),
    path('', include(book_image_router.urls)),
    path("authors/", views.AddAuthorView.as_view(), name="add_author"),
    path("authors/<int:pk>/", views.GetUpdateDeleteAuthorView.as_view(), name="GET_UPDATE_DELETE_AUTHOR"),
    path("images/<int:pk>/", views.image_detail, name="book-images-detail"),
    # path("get/authors/", views.get_authors, name="get_authors"),
    # path("authors/<int:pk>/", views.update_author, name="update_author"),
    # path("delete_author/<int:pk>/", views.delete_author, name="delete_author"),
    # path("greet/<name>", views.greet)
]