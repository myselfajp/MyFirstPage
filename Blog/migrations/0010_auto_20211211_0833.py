# Generated by Django 3.2.10 on 2021-12-11 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_auto_20211211_0828'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tags',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='tag',
        ),
    ]
