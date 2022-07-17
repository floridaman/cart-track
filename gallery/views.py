from django.views import generic
from .models import System, Game

class SystemView(generic.ListView):
    template_name = 'album.html'

    def get_queryset(self):
        return Game.objects.all()

class GameView(generic.DetailView):
    model = Game
    template_name = 'game.html'