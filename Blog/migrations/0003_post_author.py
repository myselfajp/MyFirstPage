# Generated by Django 3.2.9 on 2021-11-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Ali Parsa', max_length=255),
        ),
    ]
