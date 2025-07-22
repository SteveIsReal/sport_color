from django.db import models
from buildboard.models import Team, Game
from datetime import datetime


class EventGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Event(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    group = models.ForeignKey(EventGroup, on_delete=models.CASCADE, null=True, related_name='event_connect')

    def __str__(self):
        return f'{self.name}'

class Tournament(models.Model):
    name = models.CharField(max_length=100, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team1")
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team2")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True, related_name='tournament_connect')
    
    def __str__(self):
        return f'{self.game} : {self.team1.name} : {self.team2.name}'

class Score(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='score_connect')
    game_set = models.IntegerField(default=0)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)    

    def __str__(self):
        return f'{self.game_set} : {self.tournament.team1.name} : {self.tournament.team2.name}'

