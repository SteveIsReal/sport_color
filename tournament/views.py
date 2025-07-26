from django.shortcuts import render
from django.http import HttpResponse
from buildboard.models import Team, Game
from .models import Tournament, Score, Event, EventGroup
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from json import dumps


def tournament(request):
    content = {
        "tournaments" : Tournament.objects.all()
    }
    print('hello')
    return render(request, 'index.html', content)

def score(request):
    content = {
        "score" : Score.objects.all()
    }
    return render(request, 'score.html', content)

class TournamentAPI(APIView):
    def __create_tournament_list(self, request):
        tournament = Tournament.objects.all()
        tournament_list = list()
        for i in tournament:
            tournament_dict = dict()
            tournament_dict['event'] = i.event.name
            tournament_dict["game"] = i.game.name
            tournament_dict['team1'] = i.team1.name
            tournament_dict['team2'] = i.team2.name
            tournament_list.append(tournament_dict)
        return tournament_list

    def get(self,request):
        data = self.__create_tournament_list(request)
        return Response(status=status.HTTP_200_OK, data=data)

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

class EventAPI(APIView):

    def __create_event_group_list(self, request):
        response_data = []
        event_group = EventGroup.objects.all()

        for i in event_group:
            response_dict = dict()
            response_dict['event_group'] = i.name
            for j in i.event_connect.all():
                response_dict[j.name] = dict()
                response_dict[j.name]['place'] = j.place
                response_dict[j.name]['venue'] = j.venue
                response_dict[j.name]['date'] = j.date
                response_dict[j.name]['start_time'] = j.start_time
                response_dict[j.name]['end_time'] = j.end_time
                response_dict[j.name]['tournaments'] = dict()
                for k in j.tournament_connect.all():
                    response_dict[j.name]['tournaments'][k.name] = dict()
                    response_dict[j.name]['tournaments'][k.name]['game'] = k.game.name
                    response_dict[j.name]['tournaments'][k.name]['team1'] = {}
                    response_dict[j.name]['tournaments'][k.name]['team1']['name'] = k.team1.name
                    response_dict[j.name]['tournaments'][k.name]['team1']['status'] = k.team1.status
                    response_dict[j.name]['tournaments'][k.name]['team1']['members'] = []
                    for r in k.team1.members.all():
                        response_dict[j.name]['tournaments'][k.name]['team1']['members'].append(r.name)
                    response_dict[j.name]['tournaments'][k.name]['team2'] = {}
                    response_dict[j.name]['tournaments'][k.name]['team2']['name'] = k.team2.name
                    response_dict[j.name]['tournaments'][k.name]['team2']['status'] = k.team2.status
                    response_dict[j.name]['tournaments'][k.name]['team2']['members'] = []
                    for r in k.team2.members.all():
                        response_dict[j.name]['tournaments'][k.name]['team2']['members'].append(r.name)
                    response_dict[j.name]['tournaments'][k.name]['score'] = dict()
                    for l in k.score_connect.all():
                        response_dict[j.name]['tournaments'][k.name]['score'][f'game_set{l.game_set}'] = dict()
                        response_dict[j.name]['tournaments'][k.name]['score'][f'game_set{l.game_set}']['score1'] = l.score1 
                        response_dict[j.name]['tournaments'][k.name]['score'][f'game_set{l.game_set}']['score2'] = l.score2

            response_data.append(response_dict)
        return response_data
        
    def get(self, request):
        data = self.__create_event_group_list(request)
        return Response(status=status.HTTP_200_OK, data=data)
