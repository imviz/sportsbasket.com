# Generated by Django 4.0.4 on 2022-06-15 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_account_phone_number'),
        ('orders', '0015_alter_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.address'),
            preserve_default=False,
        ),
    ]
