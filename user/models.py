from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager
from Library_Management_System.utils import PathAndRename


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to=PathAndRename("authors/"))
    library_books_count = models.IntegerField(default=0, blank=True, null=True)

    def library_book_count(self, count=1):
        self.library_books_count += count
        self.save()

    def get_fullname(self):
        if self.middle_name is None or len(self.middle_name) <= 0:
            return f'{self.first_name} {self.surname}'
        return f'{self.first_name} {self.middle_name} {self.surname}'

    def get_absolute_url(self):
        return reverse('author_list')

    def __str__(self):
        return f'{self.first_name} {self.surname}'


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
    image = models.ImageField(null=False, upload_to=PathAndRename("borrowers/"))
    borrower_type = models.ForeignKey(BorrowerType, on_delete=models.DO_NOTHING, related_name='borrowers')
    birthdate = models.DateTimeField()
    user_created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_staff_user(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.save()
        return user
