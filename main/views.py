# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from main.models import UserInfo
<<<<<<< HEAD

from .forms import JoinForm

=======
>>>>>>> df975e563b96d347e6c53f1726ebe226a5150bdc
# Create your views here.
def home(request):
    debate_feed = {}
    template = loader.get_template('main/home.html')
    context = {
        'debate_feed': debate_feed,
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
<<<<<<< HEAD

def join(request):
    return render(request, 'main/join.html', {'form': JoinForm()})
    
=======
>>>>>>> df975e563b96d347e6c53f1726ebe226a5150bdc
