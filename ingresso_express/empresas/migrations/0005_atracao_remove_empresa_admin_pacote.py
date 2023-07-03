# Generated by Django 4.2.2 on 2023-07-02 16:53

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empresas", "0004_remove_pacote_atracoes_delete_atracao_delete_pacote"),
    ]

    operations = [
        migrations.CreateModel(
            name="Atracao",
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
                ("nome", models.CharField(max_length=200)),
                ("descricao", models.TextField()),
                (
                    "preco_fim_de_semana",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=7,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0"))
                        ],
                    ),
                ),
                (
                    "preco_feriado",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=7,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0"))
                        ],
                    ),
                ),
                ("data_expiracao", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="empresa",
            name="admin",
        ),
        migrations.CreateModel(
            name="Pacote",
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
                ("nome", models.CharField(max_length=200)),
                (
                    "preco_fim_de_semana",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=7,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0"))
                        ],
                    ),
                ),
                (
                    "preco_feriado",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=7,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0"))
                        ],
                    ),
                ),
                ("data_expiracao", models.DateField(blank=True, null=True)),
                ("atracoes", models.ManyToManyField(to="empresas.atracao")),
            ],
        ),
    ]