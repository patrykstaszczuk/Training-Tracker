# Generated by Django 3.2.8 on 2021-10-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hr_zones',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pw_zones',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
