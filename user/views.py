from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Author, Borrower
from .forms import AuthorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# USER
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('book_list')
                else:
                    return render(request, 'users/user/user_login.html', {'error': 'Disabled Account'})
            else:
                return render(request, 'users/user/user_login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/user/user_login.html')


def user_register(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        user = User.objects.create_user(username=username, email=email, first_name=first_name,
                                        last_name=last_name, password=password, )
        user.save()
    return render(request, 'users/user/user_register.html')


# AUTHOR
class AuthorListView(ListView, LoginRequiredMixin):
    login_url = ''
    model = Author
    template_name = 'users/author/author_list.html'
    paginate_by = 15


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
    template_name = 'confirm_delete.html'
