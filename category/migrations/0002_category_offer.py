# Generated by Django 4.2.5 on 2024-04-28 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("offer", "0002_remove_offer_end_date_remove_offer_is_available_and_more"),
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="offer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="offer.offer",
            ),
        ),
    ]