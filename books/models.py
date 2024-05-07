from django.db import models

class BooksCategory(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = 'BooksCategory' 

    def __str__(self) -> str:
        return f"{self.name} "
    
class BookAuthor(models.Model):
    books = models.ForeignKey('Books', on_delete=models.CASCADE)

    class Meta:
        db_table = 'BookAuthor' 
        
    def __str__(self) -> str:
        return f"{self.books} "

class Books(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    description = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    price = models.BigIntegerField()
    image = models.CharField(max_length=255)
    year = models.BigIntegerField()
    book_category = models.ForeignKey(BooksCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Books' 
        
    def __str__(self) -> str:
        return f"{self.name} "

class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    surname = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    comment = models.CharField(primary_key=True, max_length=255)
    star_given = models.BigIntegerField()
    user = models.BigIntegerField()
    book = models.ForeignKey(BookAuthor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Author' 
        
    def __str__(self) -> str:
        return f"{self.name} "

class Review(models.Model):
    comment = models.CharField(primary_key=True, max_length=255)
    star_given = models.BigIntegerField()
    user = models.BigIntegerField()
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Review' 
        
    def __str__(self) -> str:
        return f"{self.comment}"