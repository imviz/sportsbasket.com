# Generated by Django 4.0.4 on 2022-06-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
