from django.shortcuts import render, redirect
from books.models import Books
from books.forms import BooksForm

def create_book(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BooksForm()
    
    return render(request, 'create_book.html', {'form': form})

def book_detail(request, book_id):
    book = Books.objects.get(pk=book_id)
    return render(request, 'book_detail.html', {'book': book})

def update_book(request, book_id):
    book = Books.objects.get(pk=book_id)
    
    if request.method == 'POST':
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BooksForm(instance=book)
    
    return render(request, 'update_book.html', {'form': form})

def delete_book(request, book_id):
    book = Books.objects.get(pk=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    
    return render(request, 'delete_book.html', {'book': book})