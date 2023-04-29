from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from Library_Management_System.constants import AUTHOR_PAGINATE
from .forms import AuthorForm, BorrowerForm, UserForm
from .models import Author, BorrowerType, Borrower


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
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        birthdate = request.POST['birthdate']
        image = request.FILES['image']
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                        password=password1)
        user.is_staff = False
        user.is_superuser = False
        user.save()
        borrower = Borrower.objects.create(user=user,
                                           borrower_type=BorrowerType.objects.get(name__contains='Normal'),
                                           image=image,
                                           birthdate=birthdate)
        borrower.save()
        login(request, user)
        return redirect('book_list')
    if request.method == 'GET':
        context_dict = {'user_form': UserForm, 'borrower_form': BorrowerForm}
        return render(request, 'users/user/user_register.html', context=context_dict)


class RegisterView(CreateView):
    template_name = 'users/user/user_register.html'
    form_class = BorrowerForm
    success_url = reverse_lazy('book_list')


# AUTHOR
class AuthorListView(ListView, LoginRequiredMixin):
    paginate_by = AUTHOR_PAGINATE
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
    paginate_by = AUTHOR_PAGINATE
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
