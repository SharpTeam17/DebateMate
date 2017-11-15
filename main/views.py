# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from main.models import UserInfo, DailyDebate, Argument
from datetime import date

from .forms import JoinForm, TopicForm, MakePostForm

# Create your views here.
def home(request):
    return render(request, 'main/home.html')
def debate(request):
    current_user = request.user
    name = current_user.username
    profile = UserInfo.objects.get(user = current_user)
    if request.method == 'POST':
        form = MakePostForm(request.POST)
        if form.is_valid():
            temp_content = form.cleaned_data['content']
            #author, side, content
            temp_author = current_user
            temp_side = profile.current_side
            current_debate = DailyDebate.objects.filter(is_current_debate = True)[0]
            new_post = Argument(author = temp_author, side = temp_side, content = temp_content, parent_debate = current_debate)
            new_post.save()
            return render(request, 'debate')
        return render(request, 'home')
    if current_user.is_authenticated() and (profile.current_side == 'A' or profile.current_side == 'B'):
        current_debate = DailyDebate.objects.filter(is_current_debate = True)[0] #fetches debate marked current
        debate_feed = Argument.objects.filter(parent_debate = current_debate)
        debate_feed = debate_feed.order_by('-initial_post_date')
        topic = current_debate.topic
        template = loader.get_template('main/debate.html')
        form = MakePostForm()
        context = {
            'debate_feed': debate_feed,
            'name': name,
            'topic': topic,
            'form': form,
            }
        return render(request, 'main/debate.html', context)
    else:
        return render(request, 'main/login.html')

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
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            # Returns:
            # S - Spectator 
            # D - Debator
            # M - Moderator
            role = form.cleaned_data['role']
            side = form.cleaned_data['side']
            current_user = request.user
            profile = UserInfo.objects.get(user = current_user)
            profile.current_role = role
            if role == 'S' or role == 'D':
                profile.current_side = side
                profile.save()
            return redirect('home')
    else:
        form = JoinForm()
    return render(request, 'main/join.html', {'form': form})

def set_debate(request):
    current_user = request.user
    if request.method == 'POST' and current_user.is_staff:
        form = TopicForm(request.POST)
        if form.is_valid():
            #make old current debate inactive
            current_debate = DailyDebate.objects.filter(is_current_debate = True)
            for item in current_debate:
                item.is_current_debate = False
            #set new debate
            new_topic = form.cleaned_data['topic']
            debate = DailyDebate(topic = new_topic, is_current_debate = True)
            debate.save()
            return render(request, 'main/add_debate_success.html')
    elif current_user.is_staff:
        return render(request, 'main/set_debate.html', {'form': TopicForm()})
    else:
        return redirect('home')