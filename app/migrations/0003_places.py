# Generated by Django 5.0.7 on 2024-07-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('description', models.TextField(null=True)),
                ('Coordinates', models.CharField(max_length=300, null=True)),
                ('opening_hours', models.CharField(max_length=300, null=True)),
                ('contact', models.CharField(max_length=30, null=True)),
                ('rating', models.CharField(max_length=100, null=True)),
                ('agreement', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
            ],
        ),
    ]
