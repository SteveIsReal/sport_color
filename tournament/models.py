from django.db import models
from buildboard.models import Team, Game


class Tournament(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team1")
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team2")

class Score(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    game_set = models.IntegerField(default=0)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    
