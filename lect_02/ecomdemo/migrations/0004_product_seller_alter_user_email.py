# Generated by Django 5.0.6 on 2024-09-06 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecomdemo", "0003_user_address_user_title_alter_product_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="seller",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="ecomdemo.user",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(default="scaler@scaler.com", max_length=50),
        ),
    ]
