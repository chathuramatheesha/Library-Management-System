from django.db import models
from django.utils import timezone
from django.urls import reverse

from Library_Management_System.utils import PathAndRename


class Book(models.Model):
    author = models.ForeignKey('user.Author', on_delete=models.CASCADE, related_name='books')
    image = models.ImageField(null=False, upload_to=PathAndRename("books/"))
    title = models.CharField(max_length=150, blank=False, null=False)
    issued_date = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField()

    def get_absolute_url(self):
        return reverse('book_list')

    def update_quantity(self, capacity=1):
        self.quantity += capacity
        self.save()

    def __str__(self):
        return self.title


class Borrowed(models.Model):
    user = models.ForeignKey('user.Borrower', on_delete=models.CASCADE, related_name='borrowed')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowed_books')
    borrowed_date = models.DateTimeField(default=timezone.now)
    received_date = models.DateTimeField(default=timezone.now)
    late_payment_tax = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.borrowed_date)
