# Generated by Django 3.1.4 on 2022-06-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("team1_name", models.CharField(max_length=63)),
                ("team2_name", models.CharField(max_length=63)),
                ("team1_wallet", models.CharField(max_length=63)),
                ("team2_wallet", models.CharField(max_length=63)),
                ("null_wallet", models.CharField(max_length=63)),
                ("team1_cote", models.IntegerField(default=1)),
                ("team2_cote", models.IntegerField(default=1)),
                ("null_cote", models.IntegerField(default=1)),
                ("start_match_hour", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Trad",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=32, unique=True)),
                ("content", models.TextField()),
            ],
        ),
    ]
