# Generated by Django 4.1 on 2024-06-07 04:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("venadapp", "0009_alter_licenses_expiry_remainder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="licenses",
            name="licenseFile",
            field=models.ImageField(blank=True, null=True, upload_to="licenses/"),
        ),
    ]
