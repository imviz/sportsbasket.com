# Generated by Django 4.0.4 on 2022-06-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_alter_orderproduct_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='method',
            field=models.CharField(blank=True, choices=[('COD', 'COD'), ('Razorpay', 'Razorpay'), ('Pay', 'Pay')], max_length=15, null=True),
        ),
    ]
