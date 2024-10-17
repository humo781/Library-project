from django.urls import path
from . import views

urlpatterns = [
    # main url:
    path('', views.main_interface, name='main_interface'),
    # author urls:
    path('author_list/', views.author_list, name='author_list'),
    path('author_create/', views.author_create, name='author_create'),
    path('author_update/<int:pk>/edit', views.author_update, name='author_update'),
    path('author_delete/<int:pk>/delete', views.author_delete, name='author_delete'),

    # book urls:
    path('book_list/', views.book_list, name='book_list'),
    path('book_create/', views.book_create, name='book_create'),
    path('book_update/<int:pk>/edit', views.book_update, name='book_update'),
    path('book_delete/<int:pk>/delete', views.book_delete, name='book_delete'),

    # category urls:
    path('category_list/', views.category_list, name='category_list'),
    path('category_create/', views.category_create, name='category_create'),
    path('category_update/<int:pk>/edit', views.category_update, name='category_update'),
    path('category_delete/<int:pk>/delete', views.category_delete, name='category_delete'),
]
