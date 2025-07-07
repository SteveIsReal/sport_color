from tournament import views
from django.urls import path

urlpatterns = [
    path('tournament/', views.tournament),
    #path('score/', views.score),
    path('tournamentapi', views.apitournament),
    path('scoreapi', views.apiscore)
]
