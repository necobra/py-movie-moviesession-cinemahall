# Generated by Django 4.0.2 on 2024-06-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_rename_movies_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='show_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
