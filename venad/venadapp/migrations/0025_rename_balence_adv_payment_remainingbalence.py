# Generated by Django 4.1 on 2024-06-18 14:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("venadapp", "0024_adv_payment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="adv_payment",
            old_name="balence",
            new_name="remainingbalence",
        ),
    ]
