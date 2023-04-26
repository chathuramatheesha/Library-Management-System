from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.ForeignKey('user.Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False)
    issued_date = models.DateTimeField()
    quantity = models.IntegerField()

    def update_quantity(self, capacity=1):
        self.quantity += capacity
        self.save()


class Borrowed(models.Model):
    user = models.ForeignKey('user.Borrower', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(default=timezone.now)
    received_date = models.DateTimeField(default=timezone.now)
    late_payment_tax = models.IntegerField(blank=True, null=True)
