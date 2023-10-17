# Generated by Django 3.2.16 on 2023-10-16 13:10

import birthday.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0002_rename_birthdayform_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='birthday',
            field=models.DateField(validators=[birthday.validators.real_age], verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='last_name',
            field=models.CharField(blank=True, help_text='Необязательное поле', max_length=20, verbose_name='Фамилия'),
        ),
    ]