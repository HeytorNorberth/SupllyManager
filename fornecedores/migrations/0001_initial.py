# Generated by Django 5.1.1 on 2024-09-24 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fornecedor",
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
                ("nome", models.CharField(max_length=255, verbose_name="Nome")),
                ("descricao", models.TextField(verbose_name="Descrição")),
                ("is_active", models.BooleanField(verbose_name="Ativo")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="usuarios.user"
                    ),
                ),
            ],
            options={
                "verbose_name": "Fornecedor",
                "verbose_name_plural": "Fornecedores",
                "db_table": "fornecedores",
            },
        ),
    ]
