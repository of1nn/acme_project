# Generated by Django 3.2.16 on 2023-10-15 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BirthdayForm',
            new_name='Birthday',
        ),
    ]