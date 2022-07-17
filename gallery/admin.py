from django.contrib import admin
from .models import System, Game

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'system', 'boxart_tag')


admin.site.register(System)
admin.site.register(Game, GameAdmin)