# Generated by Django 4.0.4 on 2022-06-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_account_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
