# Generated by Django 5.0.6 on 2024-06-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FinancialYear",
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
                ("financial_year", models.CharField(max_length=9, null=True)),
                ("start_date", models.DateField(null=True)),
                ("end_date", models.DateField(null=True)),
            ],
        ),
    ]
