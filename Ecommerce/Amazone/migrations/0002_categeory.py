# Generated by Django 4.2.6 on 2023-12-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Amazone", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categeory",
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
                ("category_image", models.ImageField(upload_to="upload/category/")),
                (
                    "category_name",
                    models.CharField(default="", max_length=100, null=True),
                ),
            ],
        ),
    ]
