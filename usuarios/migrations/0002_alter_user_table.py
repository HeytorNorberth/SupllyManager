# Generated by Django 5.1.1 on 2024-09-24 18:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="user",
            table="usuarios",
        ),
    ]
