# Generated by Django 5.0.2 on 2024-03-10 15:15

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TouristicPoint",
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
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="tourist_spot"),
                ),
                ("approved", models.BooleanField(default=False)),
                ("complement", models.CharField(blank=True, max_length=150, null=True)),
                ("number", models.CharField(blank=True, max_length=5, null=True)),
                ("district", models.CharField(blank=True, max_length=32, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=50, null=True)),
                ("country", models.CharField(default="Brasil", max_length=70)),
                ("zip", models.CharField(blank=True, max_length=9, null=True)),
                ("latitude", models.IntegerField(blank=True, null=True)),
                ("longitude", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
