# Generated by Django 4.2.9 on 2024-01-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0003_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ratings',
            field=models.IntegerField(),
        ),
    ]
