# Generated by Django 3.1.4 on 2022-06-12 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookie", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book", name="null_cote", field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name="book", name="team1_cote", field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name="book", name="team2_cote", field=models.FloatField(default=1),
        ),
    ]