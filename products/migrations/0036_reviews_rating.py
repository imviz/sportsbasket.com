# Generated by Django 4.0.4 on 2022-06-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_reviews_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
