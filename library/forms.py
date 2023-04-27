from django import forms
from .models import Book
from user.models import Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'title', 'quantity', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
