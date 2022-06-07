from django.db import models

# Create your models here.
class Book(models.Model):
    team1_name = models.CharField(max_length=127)
    team2_name = models.CharField(max_length=127)
    team1_wallet = models.CharField(max_length=127)
    team2_wallet = models.CharField(max_length=127)
    null_wallet = models.CharField(max_length=127)
    team1_cote = models.IntegerField(default=1)
    team2_cote = models.IntegerField(default=1)
    null_cote = models.IntegerField(default=1)
    start_match_hour = models.DateTimeField()
