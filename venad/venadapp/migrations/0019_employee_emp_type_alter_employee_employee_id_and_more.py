# Generated by Django 4.1 on 2024-06-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("venadapp", "0018_employee"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="emp_type",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="employee_id",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="govt_id",
            field=models.ImageField(blank=True, null=True, upload_to="photos/"),
        ),
    ]
