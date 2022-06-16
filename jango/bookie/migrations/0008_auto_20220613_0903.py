# Generated by Django 3.1.4 on 2022-06-13 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookie", "0007_auto_20220613_0857"),
    ]

    operations = [
        migrations.RenameModel(old_name="Book", new_name="Match",),
        migrations.AddField(
            model_name="ticketcount",
            name="match",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ticket_count",
                to="bookie.match",
            ),
            preserve_default=False,
        ),
    ]