# Generated by Django 3.2.9 on 2021-12-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstsite', '0003_auto_20211207_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
