# Generated by Django 4.2.9 on 2024-01-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cate',
            field=models.CharField(default='scifi', max_length=255),
            preserve_default=False,
        ),
    ]
