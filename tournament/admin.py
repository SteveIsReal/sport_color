from django.contrib import admin
from .models import Tournament, Score, Event, EventGroup


@admin.register(Tournament)
class AdminTournament(admin.ModelAdmin):
    pass

@admin.register(Score)
class AdminScore(admin.ModelAdmin):
    pass

@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    pass

@admin.register(EventGroup)
class AdminEventGroup(admin.ModelAdmin):
    pass
