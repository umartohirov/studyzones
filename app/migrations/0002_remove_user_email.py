# Generated by Django 5.0.7 on 2024-07-27 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]