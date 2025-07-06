from django.contrib import admin
from .models import Tournament, Score


@admin.register(Tournament)
class AdminTournament(admin.ModelAdmin):
    pass

@admin.register(Score)
class AdminScore(admin.ModelAdmin):
    pass
