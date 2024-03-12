# Generated by Django 5.0.2 on 2024-03-10 15:15

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("touristic_points", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attraction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    model_utils.fields.AutoCreatedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="Criado em",
                    ),
                ),
                (
                    "updated_at",
                    model_utils.fields.AutoLastModifiedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="Modificado em",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("name", models.CharField(max_length=150)),
                ("description", models.TextField()),
                ("opening_hours", models.TextField()),
                ("minimum_age", models.PositiveIntegerField()),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="attraction"),
                ),
                (
                    "observation",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "tourist_spot",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="touristic_points.touristicpoint",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
