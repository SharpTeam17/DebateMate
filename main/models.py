# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model): #stores additional info not in built-in User model
    SIDE_CHOICES = (('A', 'A'), ('B', 'B'), ('N', 'Not on side'), ('S', 'Spectator'))
	
    user = models.ForeignKey(User, unique=True)
    current_side = models.CharField(max_length = 1, choices = SIDE_CHOICES, default = 'N')

class DailyDebate(models.Model):
	STATUS_CHOICES = (('N', 'Not started'),('O', 'Open'),('V', 'In voting'),('C', 'Complete'))
	
	#start_date = models.DateField(auto_now_add = True, null = True)
	topic = models.TextField()
	status = models.CharField(max_length = 2, choices = STATUS_CHOICES, default = 'N')
		
class Argument(models.Model):	
	SIDE_CHOICES = (('A', 'A'), ('B', 'B'))
	
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	#may want to change to SET_NULL if desired post deletion behavior is to preserve the post unless an admin is the one who deletes it
	side = models.CharField(max_length = 1, choices = SIDE_CHOICES)
	parent_debate = models.ForeignKey('DailyDebate', on_delete = models.CASCADE)
	initial_post_date = models.DateField(auto_now_add = True)
	last_edited_date = models.DateField(auto_now = True)
	content = models.TextField()

	
class Comment(models.Model):
	SIDE_CHOICES = (('A', 'A'), ('B', 'B'))
	
	parent_post = models.ForeignKey(Argument)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	side = models.CharField(max_length = 1, choices = SIDE_CHOICES)
	parent_debate = models.ForeignKey('DailyDebate', on_delete = models.CASCADE)
	initial_post_date = models.DateField(auto_now_add = True)
	last_edited_date = models.DateField(auto_now = True)
	content = models.TextField()