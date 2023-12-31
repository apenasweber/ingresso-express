# Generated by Django 4.2.2 on 2023-06-27 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("empresas", "0002_remove_empresa_admin"),
    ]

    operations = [
        migrations.AddField(
            model_name="empresa",
            name="admin",
            field=models.OneToOneField(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
