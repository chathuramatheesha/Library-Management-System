# Generated by Django 4.2 on 2023-04-29 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_borrowertype_borrowed_books_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='borrowed_books',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
