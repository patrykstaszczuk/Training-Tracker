# Generated by Django 3.2.8 on 2021-10-24 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training_api', '0002_auto_20211015_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='weigth',
        ),
    ]