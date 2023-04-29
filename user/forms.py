from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Author, Borrower


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'middle_name', 'surname', 'image')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        form_control_css = {'class': 'form-control'}
        widgets = {
            'first_name': forms.TextInput(attrs=form_control_css),
            'last_name': forms.TextInput(attrs=form_control_css),
            'username': forms.TextInput(attrs=form_control_css),
            'password1': forms.PasswordInput(attrs=form_control_css),
            'password2': forms.PasswordInput(attrs=form_control_css),
        }


class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ('birthdate', 'image')
        labels = {'birthdate': 'Birth Date', 'image': 'Profile Picture'}
        widgets = {
            'birthdate': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd', 'id': 'datepicker'})
        }
