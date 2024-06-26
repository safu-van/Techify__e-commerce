# Generated by Django 4.2.5 on 2024-05-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0011_remove_orders_sub_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="razorpay_order_id",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="orders",
            name="razorpay_payment_id",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="orders",
            name="razorpay_signature",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
