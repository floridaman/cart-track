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

class SystemView(generic.ListView):
    template_name = 'album.html'

    def get_queryset(self):
        return Game.objects.all()

class GameView(generic.DetailView):
    model = Game
    template_name = 'game.html'

@login_required(login_url=reverse_lazy('login'))
def add(request, game_id):
    user = request.user
    game = get_object_or_404(Game, pk=game_id)
    collection = get_object_or_404(Collection, pk=user.id)

    return HttpResponseRedirect(reverse('gallery:defaultgallery'))

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