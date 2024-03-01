# Generated by Django 4.2.9 on 2024-02-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_review_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='count_rating',
            field=models.IntegerField(default=0),
        ),
    ]
