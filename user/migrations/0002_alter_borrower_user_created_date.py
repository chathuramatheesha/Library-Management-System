# Generated by Django 4.2 on 2023-04-26 00:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='user_created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 0, 31, 36, 837402, tzinfo=datetime.timezone.utc)),
        ),
    ]
