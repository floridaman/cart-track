from django.views import generic
from .models import System, Game, Collection
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CollectionView(generic.ListView):
    template_name = 'album.html'

    def get_queryset(self):
        user_collection = Collection.objects.filter(user=self.request.user.id).first().games.all()
        return user_collection
    
    def get_context_data(self, **kwargs):
        context = super(generic.ListView, self).get_context_data(**kwargs)
        context['type'] = 'collection'
        return context

class SystemView(generic.ListView):
    template_name = 'album.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            unowned_games = Game.objects.exclude(id__in=Collection.objects.filter(user=self.request.user.id).first().games.all())
            # user_collection = Collection.objects.filter(user=self.request.user.id).first().games.all()
            return unowned_games
        else:
            return Game.objects.all()

class GameView(generic.DetailView):
    model = Game
    template_name = 'game.html'

@login_required(login_url=reverse_lazy('login'))
def add(request, game_id):
    user = request.user
    game = get_object_or_404(Game, pk=game_id)
    collection = get_object_or_404(Collection, user=user)
    collection.games.add(game)

    return HttpResponseRedirect(reverse('gallery:defaultgallery'))

@login_required(login_url=reverse_lazy('login'))
def remove(request, game_id):
    user = request.user
    game = get_object_or_404(Game, pk=game_id)
    collection = get_object_or_404(Collection, user=user)
    collection.games.remove(game)

    return HttpResponseRedirect(reverse('gallery:collection'))

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        userModel = get_user_model()
        user = get_object_or_404(userModel, username=form.cleaned_data['username'])
        collection = Collection(user=user)
        collection.save()
        print ("test" + self.success_url)
        return HttpResponseRedirect(self.success_url)