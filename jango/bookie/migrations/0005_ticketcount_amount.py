# Generated by Django 3.1.4 on 2022-06-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookie", "0004_auto_20220613_0735"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticketcount",
            name="amount",
            field=models.IntegerField(default=0),
        ),
    ]
