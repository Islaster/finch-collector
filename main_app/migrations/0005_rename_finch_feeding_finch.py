# Generated by Django 4.0.1 on 2022-01-17 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_toy_finch_toy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeding',
            old_name='finch',
            new_name='Finch',
        ),
    ]