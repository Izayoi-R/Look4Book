# Generated by Django 3.2.25 on 2024-08-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='books_cover',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
