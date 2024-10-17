from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category, Author
from .forms import AuthorForm, CategoryForm, BookForm


# Author views
@login_required
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author/author_list.html', {'authors': authors})

@login_required
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
        return render(request, 'author/author_create.html', {'form': form})

@login_required
def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.first_name = request.POST.get('name')
        author.last_name = request.POST.get('last_name')
        author.save()
        return redirect('author_list')
    return render(request, 'author/author_update.html', {'author': author})

@login_required
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'author/author_delete.html', {'author': author})


# Book views
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            return render(request, 'book/book_create.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'book/book_create.html', {'form': form})

@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.save()
        return redirect('book_list')
    return render(request, 'book/book_update.html', {'book': book})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book/book_delete.html', {'book': book})


# Category views
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
        return render(request, 'category/category_create.html', {'form': form})

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('category_list')
    return render(request, 'category/category_update.html', {'category': category})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category/category_delete.html', {'category': category})


def main_interface(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()
    ctx = {'categories': categories,
           'books': books,
           'authors': authors}
    return render(request, 'main_interface.html', ctx)
