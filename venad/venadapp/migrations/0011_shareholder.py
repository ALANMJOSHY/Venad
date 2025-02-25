# Generated by Django 4.1 on 2024-06-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("venadapp", "0010_alter_licenses_licensefile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shareholder",
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
                ("shareholder_name", models.CharField(max_length=255)),
                ("shareholder_id", models.CharField(max_length=20, unique=True)),
                ("address", models.CharField(max_length=255)),
                ("pin", models.CharField(max_length=6)),
                ("age", models.PositiveIntegerField()),
                ("phone", models.CharField(max_length=15)),
                ("dob", models.DateField()),
                ("joining_date", models.DateField()),
                ("aadhar", models.CharField(max_length=12, unique=True)),
                ("pan", models.CharField(max_length=10, unique=True)),
                ("bank_name", models.CharField(max_length=255)),
                ("account_number", models.CharField(max_length=20, unique=True)),
                ("branch", models.CharField(max_length=255)),
                ("ifsc", models.CharField(max_length=11)),
                (
                    "opening_balance",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("no_of_shares", models.PositiveIntegerField()),
                ("dhalam", models.CharField(max_length=255)),
                ("nominee_name", models.CharField(max_length=255)),
                ("relation", models.CharField(max_length=255)),
                (
                    "annual_turnover",
                    models.DecimalField(decimal_places=2, max_digits=15),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="shareholder_photos/"
                    ),
                ),
                (
                    "signature",
                    models.ImageField(
                        blank=True, null=True, upload_to="shareholder_signatures/"
                    ),
                ),
            ],
        ),
    ]
