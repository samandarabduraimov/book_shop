from django.contrib import admin
from .models import Books , BookAuthor , BooksCategory ,Review , Author
# Register your models here.
admin.site.register(Books)
admin.site.register(BookAuthor)
admin.site.register(BooksCategory)
admin.site.register(Review)
admin.site.register(Author)