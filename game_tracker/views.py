from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def index(request):
    return render(request, 'base.html')

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url: reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)