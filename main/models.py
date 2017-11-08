# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	ROLE_CHOICES = (('S', 'Spectator'),('D', 'Debater'),('A', 'Administrator'))
	
	username = models.CharField(max_length = 15, unique = True)
	current_role = models.CharField(max_length = 1, choices = ROLE_CHOICES, default = 'S')
	admin_capable = models.BooleanField(default = 'N') #whether or not the user is allowed to switch to admin role

class DailyDebate(models.Model):
	STATUS_CHOICES = (('N', 'Not started'),('O', 'Open'),('V', 'In voting'),('C', 'Complete'))
	
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