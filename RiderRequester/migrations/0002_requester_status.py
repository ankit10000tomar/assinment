# Generated by Django 3.2.16 on 2023-01-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiderRequester', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requester',
            name='Status',
            field=models.CharField(default='Pending', max_length=180),
        ),
    ]