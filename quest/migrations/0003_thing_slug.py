# Generated by Django 4.1.7 on 2023-03-02 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quest", "0002_alter_quest_options_alter_thing_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="thing",
            name="slug",
            field=models.SlugField(default="tmp"),
            preserve_default=False,
        ),
    ]
