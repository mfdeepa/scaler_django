# Generated by Django 5.1.1 on 2024-09-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecomdemo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=50)),
                ("price", models.FloatField()),
                ("description", models.TextField()),
                ("stock", models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
