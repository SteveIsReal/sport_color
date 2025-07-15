from django.shortcuts import render
from django.http import HttpResponse
from buildboard.models import Team, Game
from .models import Tournament, Score, Event, EventGroup
from json import dumps


def tournament(request):
    content = {
        "tournaments" : Tournament.objects.all()
    }
    return render(request, 'index.html', content)

def score(request):
    content = {
        "score" : Score.objects.all()
    }
    return render(request, 'score.html', content)

def apitournament(request):
    response_data = []
    for i in Tournament.objects.all():
        data = {}
        data['game'] = i.game.name
        data['team1'] = i.team1.name
        data['team2'] = i.team2.name
        response_data.append(data)

    return HttpResponse(dumps(response_data))

def apiscore(request):
    response_data = []
    for score in Score.objects.all():
        data = {}
        data['game'] = score.tournament.game.name
        data['game_set'] = score.game_set
        data['team1'] = {}
        data['team1']['color'] = score.tournament.team1.color
        data['team1']['name'] = score.tournament.team1.name
        data['team1']['score'] = score.score1
        data['team2'] = {}
        data['team2']['color'] = score.tournament.team1.color
        data['team2']['name'] = score.tournament.team1.name
        data['team2']['score'] = score.score2
        response_data.append(data)

    return HttpResponse(dumps(response_data))

def apiall(request):
    response_data = []

