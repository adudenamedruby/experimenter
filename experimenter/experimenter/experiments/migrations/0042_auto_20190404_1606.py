# Generated by Django 2.1.7 on 2019-04-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("experiments", "0041_auto_20190403_2037")]

    operations = [
        migrations.AlterField(
            model_name="experimentvariant",
            name="value",
            field=models.TextField(null=True),
        )
    ]