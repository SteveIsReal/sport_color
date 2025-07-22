from tournament import views
from django.urls import path

urlpatterns = [
    path('tournament/', views.tournament),
    #path('score/', views.score),
    path('tournamentapi', views.TournamentAPI.as_view()),
    path('scoreapi', views.apiscore),
    path('eventapi', views.EventAPI.as_view())
]
