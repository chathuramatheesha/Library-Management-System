# Generated by Django 4.2 on 2023-04-26 00:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_borrower_user_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='issued_books_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='library_books_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='user_created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 0, 32, 31, 245888, tzinfo=datetime.timezone.utc)),
        ),
    ]