# Generated by Django 4.0.4 on 2022-06-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_order_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='method',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='method',
            field=models.CharField(blank=True, choices=[('Razorpay', 'Razorpay'), ('COD', 'COD'), ('Pay', 'Pay')], max_length=15, null=True),
        ),
    ]