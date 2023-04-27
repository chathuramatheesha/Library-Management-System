from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('search/', views.BookSearchView.as_view(), name='book_search'),
    path('add/', views.BookCreateView.as_view(), name='book_add'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
]
