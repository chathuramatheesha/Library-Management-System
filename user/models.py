from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=150, blank=False, null=False)
    issued_books_count = models.IntegerField()
    library_books_count = models.IntegerField()

    def add_issued_book(self, count=1):
        self.issued_books_count += count
        self.save()

    def library_book_count(self, count=1):
        self.library_books_count += count
        self.save()

    def __str__(self):
        return f'{self.first_name} {self.middle_name}'


class BorrowerType(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    how_many_books_can_be_borrowed = models.IntegerField(blank=False, null=False)
    late_payment_rate = models.FloatField(blank=False, null=False)

    def update_borrowed_book_count(self, capacity: int):
        self.how_many_books_can_be_borrowed = capacity
        self.save()

    def update_late_payment_rate(self, rate: float):
        self.late_payment_rate = rate
        self.save()

    def __str__(self):
        return self.name


class Borrower(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    borrower_type = models.ForeignKey(BorrowerType, on_delete=models.DO_NOTHING)
    birthdate = models.DateTimeField()
    user_created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
