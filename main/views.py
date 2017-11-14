# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from main.models import UserInfo, DailyDebate
from datetime import date

from .forms import JoinForm, TopicForm

# Create your views here.
def home(request):
	
    debate_feed = {}
    current_user = request.user
    name = current_user.username
    template = loader.get_template('main/spectator.html')
    context = {
        'debate_feed': debate_feed,
		'name': name
    }
    return HttpResponse(template.render(context, request))


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

def set_debate(request):
    current_user = request.user
    if request.method == 'POST' and current_user.is_staff:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.cleaned_data['topic']
            debate = DailyDebate(topic = new_topic)
            debate.start_date = date.today()
            debate.save()
            return render(request, 'main/add_debate_success.html')
    elif current_user.is_staff:
        return render(request, 'main/set_debate.html', {'form': TopicForm()})
    else:
        return redirect('home')