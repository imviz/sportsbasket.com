# Generated by Django 4.0.4 on 2022-06-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_reviews_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
