# Generated by Django 3.0.5 on 2020-04-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_location',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
