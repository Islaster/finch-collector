# Generated by Django 4.0.1 on 2022-01-22 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_finch_feeding_finch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finch',
            old_name='toy',
            new_name='toys',
        ),
    ]
