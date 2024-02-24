# Generated by Django 5.0.2 on 2024-02-21 00:36

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
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
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Nome"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={"unique": "Usuário com e-mail já existente."},
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Telefone"
                    ),
                ),
                (
                    "document",
                    models.CharField(
                        blank=True, max_length=40, null=True, verbose_name="Documento"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("male", "Masculino"), ("female", "Feminino")],
                        max_length=50,
                        null=True,
                        verbose_name="Gênero",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data de Nascimento"
                    ),
                ),
                (
                    "nationality",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Nacionalidade",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="País"
                    ),
                ),
                (
                    "zipcode",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="CEP"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Cidade"
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        blank=True, max_length=2, null=True, verbose_name="Estado"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Endereço"
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Número"
                    ),
                ),
                (
                    "district",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Bairro"
                    ),
                ),
                (
                    "complement",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Complemento",
                    ),
                ),
                (
                    "agent",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Dispositivo",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="Ativo?",
                    ),
                ),
                (
                    "type",
                    models.PositiveIntegerField(
                        blank=True,
                        choices=[(0, "admin"), (1, "customer")],
                        default=1,
                        editable=False,
                        verbose_name="Tipo de Usuário",
                    ),
                ),
                (
                    "expires_in",
                    models.DateField(
                        blank=True, null=True, verbose_name="Assinatura Expira em:"
                    ),
                ),
                (
                    "register_ip",
                    models.GenericIPAddressField(
                        blank=True, null=True, verbose_name="IP de Registro"
                    ),
                ),
                (
                    "last_ip_login",
                    models.GenericIPAddressField(blank=True, editable=False, null=True),
                ),
                (
                    "register_agent",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Dispositivo",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuário",
                "verbose_name_plural": "Todos os usuários",
            },
        ),
        migrations.CreateModel(
            name="Admin",
            fields=[],
            options={
                "verbose_name": "Administrador",
                "verbose_name_plural": "Administradores",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("accounts.user",),
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[],
            options={
                "verbose_name": "Inscrito",
                "verbose_name_plural": "Inscritos",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("accounts.user",),
        ),
    ]
