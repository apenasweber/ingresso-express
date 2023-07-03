# Generated by Django 4.2.2 on 2023-07-02 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("empresas", "0005_atracao_remove_empresa_admin_pacote"),
    ]

    operations = [
        migrations.CreateModel(
            name="Insight",
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
                ("acessos_pagina_principal", models.PositiveIntegerField(default=0)),
                ("acessos_pagina_atracao", models.PositiveIntegerField(default=0)),
                ("acessos_pagina_pacote", models.PositiveIntegerField(default=0)),
                ("vendas_realizadas", models.PositiveIntegerField(default=0)),
                ("data", models.DateField(auto_now_add=True)),
                (
                    "atracao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="empresas.atracao",
                    ),
                ),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="empresas.empresa",
                    ),
                ),
                (
                    "pacote",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="empresas.pacote",
                    ),
                ),
            ],
        ),
    ]
