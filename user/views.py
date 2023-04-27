from django.db.models import Q
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Author, Borrower
from .forms import AuthorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# AUTHOR
class AuthorListView(ListView, LoginRequiredMixin):
    login_url = ''
    model = Author
    template_name = 'users/author/author_list.html'


class AuthorCreateView(CreateView, LoginRequiredMixin):
    login_url = ''
    model = Author
    form_class = AuthorForm
    template_name = 'users/author/author_add.html'
    redirect_field_name = 'author_list'


class AuthorSearchView(ListView, LoginRequiredMixin):
    login_url = ''
    model = Author
    template_name = 'users/author/author_list.html'

    def get_queryset(self):
        query = self.request.GET.get('book_search')
        author_list = Author.objects.filter(
            Q(first_name__icontains=query) | Q(middle_name__icontains=query) | Q(surname__icontains=query)
        )
        return author_list


class AuthorUpdateView(UpdateView, LoginRequiredMixin):
    login_url = ''
    model = Author
    redirect_field_name = 'author_list'
    form_class = AuthorForm
    template_name = 'users/author/author_add.html'


class AuthorDeleteView(DeleteView, LoginRequiredMixin):
    login_url = ''
    model = Author
    success_url = reverse_lazy('author_list')
    template_name = 'users/author/../templates/confirm_delete.html'


# USER
def login(request):
    return render(request, 'users/user/user_login.html')
