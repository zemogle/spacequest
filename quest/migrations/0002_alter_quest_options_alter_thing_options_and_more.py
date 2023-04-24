# Generated by Django 4.1.7 on 2023-02-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quest", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="quest", options={"ordering": ["name", "active"]},
        ),
        migrations.AlterModelOptions(name="thing", options={"ordering": ["name"]},),
        migrations.AddField(
            model_name="quest",
            name="location",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="quest",
            name="pluscode",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="quest",
            name="threewords",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
