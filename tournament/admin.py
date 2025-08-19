from django.contrib import admin
from .models import Tournament, Score, Event, EventGroup, MatchScoreBoard, Branch


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

@admin.register(Branch)
class AdminBranch(admin.ModelAdmin):
    pass

@admin.register(MatchScoreBoard)
class AdminMatch(admin.ModelAdmin):
    pass
