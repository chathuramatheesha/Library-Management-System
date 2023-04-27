from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Borrowed
from Library_Management_System.constants import LIBRARY_QUOTE, BRAND_NAME


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['library_quote'] = LIBRARY_QUOTE
        context['brand_name'] = BRAND_NAME
        return context


class BookSearchView(ListView):
    model = Book
    template_name = 'books/book_list.html'

    def get_queryset(self):
        query = self.request.GET.get('book_search')
        book_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__first_name__icontains=query) | Q(
                author__surname__icontains=query) | Q(author__middle_name__icontains=query)
        )
        return book_list


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
