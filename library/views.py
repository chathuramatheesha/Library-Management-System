from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from Library_Management_System.constants import BOOK_PAGINATE
from user.models import Borrower
from .forms import BookForm
from .models import Book, Borrowed


class BookListView(ListView):
    paginate_by = BOOK_PAGINATE
    model = Book
    template_name = 'books/book_list.html'


class BookSearchView(ListView):
    paginate_by = BOOK_PAGINATE
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


@login_required(login_url='user_login')
def borrow_book(request, pk):
    context = {}
    if request.user is not None:
        user = Borrower.objects.get(user=request.user)
        book = Book.objects.get(pk=pk)
        try:
            borrowed = Borrowed.objects.get(user=user, book=book)
        except Borrowed.DoesNotExist:
            borrowed = None
        if user.borrowed_books < user.borrower_type.how_many_books_can_be_borrowed:
            if borrowed is None:
                borrow = Borrowed.objects.create(user=user, book=book)
                context['book'] = book
                context['borrow'] = borrow
                context['received_date'] = borrow.borrowed_date + timedelta(weeks=2)
                borrow.save()
                book.quantity -= 1
                user.borrowed_books += 1
                user.save()
                book.save()
            else:
                context['error'] = 'You already borrow this book'
        else:
            context['error'] = 'You cannot borrow any more books'
        return render(request, 'books/book_borrowed.html', context=context)
