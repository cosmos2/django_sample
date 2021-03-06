# Generated by Django 3.2.6 on 2021-08-03 17:42

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Letter",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name="modified"),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                ("title", models.CharField(blank=True, max_length=24, null=True, verbose_name="제목")),
                ("content", models.TextField(verbose_name="내용")),
            ],
        ),
    ]
