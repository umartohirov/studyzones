# Generated by Django 5.0.7 on 2024-07-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='location',
            field=models.TextField(),
        ),
    ]