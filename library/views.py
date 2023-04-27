from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Book, Borrowed
from user.models import Author
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookForm
from django.urls import reverse_lazy


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    paginate_by = 15


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


class BookDeleteView(DeleteView, LoginRequiredMixin):
    login_url = ''
    model = Book
    success_url = reverse_lazy('book_list')
    template_name = 'confirm_delete.html'


class BookCreateView(CreateView, LoginRequiredMixin):
    login_url = ''
    model = Book
    form_class = BookForm
    template_name = 'books/book_add.html'
    redirect_field_name = 'book_list'


class BookUpdateView(UpdateView, LoginRequiredMixin):
    login_url = ''
    model = Book
    redirect_field_name = 'book_list'
    form_class = BookForm
    template_name = 'books/book_add.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
