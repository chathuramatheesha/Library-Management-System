# Generated by Django 4.2 on 2023-04-25 15:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('surname', models.CharField(max_length=150)),
                ('issued_books_count', models.IntegerField(max_length=3)),
                ('library_books_count', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('how_many_books_can_be_borrowed', models.IntegerField()),
                ('late_payment_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateTimeField()),
                ('user_created_date', models.DateTimeField(default=datetime.datetime(2023, 4, 25, 15, 49, 25, 813230, tzinfo=datetime.timezone.utc))),
                ('borrower_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.borrowertype')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]