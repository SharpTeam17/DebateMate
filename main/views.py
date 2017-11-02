# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    debate_feed = {}
    template = loader.get_template('main/home.html')
    context = {
        'debate_feed': debate_feed,
    }
    return HttpResponse(template.render(context, request))
