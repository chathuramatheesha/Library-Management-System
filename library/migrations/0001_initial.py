# Generated by Django 4.2 on 2023-04-29 02:41

import Library_Management_System.utils
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=Library_Management_System.utils.PathAndRename('books/'))),
                ('title', models.CharField(max_length=150)),
                ('issued_date', models.DateField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='user.author')),
            ],
        ),
        migrations.CreateModel(
            name='Borrowed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateField(default=django.utils.timezone.now)),
                ('received_date', models.DateField(blank=True, null=True)),
                ('late_payment_tax', models.IntegerField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to='library.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed', to='user.borrower')),
            ],
        ),
    ]
