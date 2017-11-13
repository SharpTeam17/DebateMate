# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from main.models import UserInfo

from .forms import JoinForm

# Create your views here.
def home(request):
    debate_feed = {}
    context = {
        'debate_feed': debate_feed
    }
    return render(request, 'main/spectator.html', context)

def rules(request):
    context = {
        'data': 'string data'
    }
    return render(request, 'main/rules.html', context)

def help(request):
    context = {
        'data': 'string data'
    }
    return render(request, 'main/help.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = UserInfo(user=user, current_side='N')
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

def join(request):
    return render(request, 'main/join.html', {'form': JoinForm()})
