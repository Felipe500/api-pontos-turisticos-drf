# Generated by Django 5.0.2 on 2024-03-11 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("touristic_points", "0003_touristicpoint_reviews"),
    ]

    operations = [
        migrations.RenameField(
            model_name="touristicpoint",
            old_name="reviews",
            new_name="number_reviews",
        ),
        migrations.RenameField(
            model_name="touristicpoint",
            old_name="total_reviews",
            new_name="total_review",
        ),
    ]
