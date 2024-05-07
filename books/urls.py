from django.urls import path
from .views import  create_book, update_book, book_detail, delete_book


app_name = 'books'
urlpatterns = [
    path('books/<int:pk>', create_book, name='create_book'),
    path('products/detail/<int:pk>', book_detail, name='book_detail'),
    path('add_products', update_book, name='update_book'),
    path('update/<int:pk>', delete_book, name='delete_book'),
]