from django.contrib import admin
from .models import Student, Game, Team

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    pass

@admin.register(Team)
class AdminTeam(admin.ModelAdmin):
    pass

@admin.register(Game)
class AdminGame(admin.ModelAdmin):
    pass
