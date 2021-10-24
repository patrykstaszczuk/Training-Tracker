# Generated by Django 3.2.8 on 2021-10-24 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthDiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weigth', models.FloatField(null=True)),
                ('rest_hr', models.IntegerField(null=True)),
                ('morning_sress_score', models.IntegerField(null=True)),
                ('evening_stress_score', models.IntegerField(null=True)),
                ('moring_mood', models.IntegerField(null=True)),
                ('evening_mood', models.IntegerField(null=True)),
                ('sleep_length', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
