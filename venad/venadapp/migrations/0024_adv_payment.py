# Generated by Django 4.1 on 2024-06-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("venadapp", "0023_products"),
    ]

    operations = [
        migrations.CreateModel(
            name="Adv_payment",
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
                ("date", models.DateField(null=True)),
                ("amount", models.CharField(max_length=50, null=True)),
                ("balence", models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
