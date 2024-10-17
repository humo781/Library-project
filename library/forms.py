from django import forms
from .models import Book, Author, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_at', 'isbn', 'pages', 'language', 'category', 'added_at_to_library']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'bio']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
