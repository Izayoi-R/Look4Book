# Generated by Django 3.2.25 on 2024-08-18 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13)),
                ('title', models.CharField(max_length=50, null=True)),
                ('author', models.CharField(max_length=20, null=True)),
                ('publisher', models.CharField(max_length=20, null=True)),
                ('overview', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('books', models.ManyToManyField(to='api.Book')),
            ],
        ),
    ]
