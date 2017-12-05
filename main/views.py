# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from main.models import UserInfo, DailyDebate, Argument, Comment, Rubric
from datetime import date, datetime

from .forms import JoinForm, JoinFormMod, TopicForm, MakePostForm, MakeCommentForm, ReportForm, ScoreArgumentForm
from django.template.defaulttags import register

@register.filter #allows looking up a value to a dictionary within a template when the value is part of a loop
def get_item(dictionary, key):
    return dictionary.get(key)
#usage: {{ dicotionary_name|get_item:value }}

def make_context(current_user, debate_id):
    #fetches necessary items to render a debate page
    name = current_user.username
    profile = UserInfo.objects.get(user = current_user)
    role = profile.current_role
    current_debate = DailyDebate.objects.get(id = debate_id) #fetches debate marked current
    debate_feed = Argument.objects.filter(parent_debate = current_debate)
    debate_feed = debate_feed.filter(isActive = True)
    debate_feed = debate_feed.order_by('-initial_post_date')
    comment_set = Comment.objects.filter(parent_debate=current_debate)
    comment_set = comment_set.filter(isActive = True)

    comments = {} #dict where key = parent argument and value = list of child comments
    scores = {} #dict where key = argument id and value = average of scores it has received
    counters = {} #dict where key = argument id and value = number of times it has been scored
    a_total = 0 # raw points total for side a
    a_scores = 0 # numver of times any argument from side a has been scored
    b_total = 0
    b_scores = 0

    for item in debate_feed:
        #create comments[] entry for each post
        comments[item] = comment_set.filter(parent_post=item)

        #create scores[] and counters[] entry for each post when applicable
        side = item.side
        temp_scores = Rubric.objects.filter(post = item)
        count = 0
        point_total = 0
        if temp_scores:
            for score in temp_scores:
                point_total += score.total
                count += 1
                if side == 'A':
                    a_total += score.total
                    a_scores += 1
                elif side == 'B':
                    b_total += score.total
                    b_scores += 1
            try:
                scores[item.id] = point_total / count
                counters[item.id] = count
            except ZeroDivisionError:
                pass

    #to avoid dividing by zero, the average score is set to 0 if a side has not received any scores. The template displays a custom message in this case.
    if a_scores == 0:
        a_average = 0
    else:
        a_average = a_total / a_scores

    if b_scores == 0:
        b_average = 0
    else:
        b_average = b_total / b_scores

    topic = current_debate.topic
    post_form = MakePostForm()
    comment_form = MakeCommentForm()

    a_bar = a_average * 4
    b_bar = b_average * 4

    context = {
        'debate_feed': debate_feed,
        'comments': comments,
        'name': name,
        'role': role,
        'topic': topic,
        'post_form': post_form,
        'comment_form': comment_form,
        'scores': scores,
        'a_average': a_average,
        'a_scores': a_scores,
        'b_average': b_average,
        'b_scores': b_scores,
        'counters': counters,
        'a_bar': a_bar,
        'b_bar': b_bar,
        }
    return context

# Create your views here.
def home(request):
    #redirect user as appropriate:
        #not logged in = go to log in page (until top comments or other preview is implemented)
        #no role goes to join page
        #Spectator goes to spectator view regardless of other factors
        #mod goes to admin page regardless of other factors
        #debater goes to join page if no side, goes to debate page if side chosen
    current_user = request.user
    if current_user.is_staff and (not UserInfo.objects.filter(user = current_user)):
        profile = UserInfo(user = current_user, current_role = 'M', current_side = 'N')
        profile.save()
    if current_user.is_authenticated:
        profile = UserInfo.objects.get(user = current_user)
        if profile.current_role == 'N':
            return redirect('join')
        elif profile.current_role == 'S':
            return redirect('spectate')
        elif profile.current_role == 'M' and current_user.is_staff:
            return redirect('moderate')
        elif profile.current_role == 'D':
            if profile.current_side == 'A' or profile.current_side == 'B':
                return redirect('debate')
            else:
                return redirect('join')
        return redirect('join')
    else:
        return redirect('login')

def debate(request):
    current_user = request.user
    name = current_user.username
    profile = UserInfo.objects.get(user = current_user)

    if request.method == 'POST': #if page was reached after submitting form...
        if 'comment_submit' in request.POST: #differentiate between comment form or post form
            comment_form = MakeCommentForm
            if form.is_valid():
                temp_content = form.cleaned_data['content']
                #temp_parent =
                temp_author = current_user
                temp_side = profile.current_side
                current_debate = DailyDebate.objects.get(is_current_debate = True)
                new_post = Argument(author = temp_author, side = temp_side, content = temp_content, parent_debate = current_debate)
                new_post.save()
                current_debate = DailyDebate.objects.get(is_current_debate = True) #fetches debate marked current
                context = make_context(current_user, current_debate.id)

                return render(request, 'main/debate.html', context)

        if 'post_submit' in request.POST:
            form = MakePostForm(request.POST)
            if form.is_valid():
                temp_content = form.cleaned_data['content']
                temp_source = form.cleaned_data['source']
                temp_author = current_user
                temp_side = profile.current_side
                current_debate = DailyDebate.objects.get(is_current_debate = True)
                new_post = Argument(author = temp_author, side = temp_side, content = temp_content, source = temp_source, parent_debate = current_debate)
                new_post.save()
                current_debate = DailyDebate.objects.get(is_current_debate = True) #fetches debate marked current
                context = make_context(current_user, current_debate.id)
                return render(request, 'main/debate.html', context)

    #check if user is logged in, a debater, and on a side
    if current_user.is_authenticated() and (profile.current_side == 'A' or profile.current_side == 'B') and (profile.current_role == 'D'):
        current_debate = DailyDebate.objects.get(is_current_debate = True) #fetches debate marked current
        context = make_context(current_user, current_debate.id)
        return render(request, 'main/debate.html', context)
    else:
        return render(request, 'main/login.html')

def moderate(request):
    return render(request, 'main/moderate.html')

def view_reported_arguments(request):
    current_user = request.user
    if current_user.is_staff:
        reported_arguments_feed = Argument.objects.filter(isReported = True)
        reported_arguments_feed = reported_arguments_feed.order_by('-reportedDate')
        context = {
            'reported_arguments_feed': reported_arguments_feed
        }
        return render(request, 'main/view_reported_arguments.html', context)
    else:
        return render(request, 'main/staff_only.html')


def view_reported_comments(request):
    current_user = request.user
    if current_user.is_staff:
        reported_comments_feed = Comment.objects.filter(isReported = True)
        reported_comments_feed = reported_comments_feed.order_by('-reportedDate')
        context = {
            'reported_comments_feed': reported_comments_feed
        }
        return render(request, 'main/view_reported_comments.html', context)
    else:
        return render(request, 'main/staff_only.html')

def view_closed_debate(request):
    current_user = request.user
    scored_arguments_temp = Rubric.objects.filter(grader = current_user)
    scored_arguments = []
    for item in scored_arguments_temp:
        scored_arguments.append(item.post_id)

    debate_id = request.GET.get('debate_id')
    context = make_context(current_user, debate_id)
    context['scored_arguments'] = scored_arguments
    return render(request, 'main/view_closed_debate.html', context)

def closed_debate_list(request):
    current_user = request.user
    #scored_arguments_temp = Rubric.objects.filter(grader = current_user)
    #scored_arguments = []
    #for item in scored_arguments_temp:
    #    scored_arguments.append(item.post_id)
    debate_list = DailyDebate.objects.filter(is_current_debate = False)
    debate_list = debate_list.order_by('-start_date')
    context = {
        'debate_list': debate_list
    }
    #context['scored_arguments'] = scored_arguments
    return render(request, 'main/closed_debate_list.html', context)

def spectate(request):
    current_user = request.user
    scored_arguments_temp = Rubric.objects.filter(grader = current_user)
    scored_arguments = []
    for item in scored_arguments_temp:
        scored_arguments.append(item.post_id)
    current_debate = DailyDebate.objects.get(is_current_debate = True) #fetches debate marked current
    context = make_context(current_user, current_debate.id)
    context['scored_arguments'] = scored_arguments
    return render(request, 'main/spectate.html', context)

def report_argument(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            post_id = form.cleaned_data['post_id']
            reportedArgument = Argument.objects.get(id = post_id)
            reportedArgument.isReported = True
            reportedArgument.reasonForBeingReported = reason
            reportedArgument.reportedDate = datetime.now()
            reportedArgument.save()
            return redirect('spectate')
    else:
        post_id = request.GET.get('post_id')
        reportedArgument = Argument.objects.get(id = post_id)
        form = ReportForm(initial = {'post_id': post_id})
        context = {
            'reportedArgument': reportedArgument,
            'form': form
            }
    return render(request, 'main/report_argument.html', context)

def report_comment(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            post_id = form.cleaned_data['post_id']
            reportedComment = Comment.objects.get(id = post_id)
            reportedComment.isReported = True
            reportedComment.reasonForBeingReported = reason
            reportedComment.reportedDate = datetime.now()
            reportedComment.save()
            return redirect('spectate')
    else:
        #using post_id for name instead of comment_id here since the report form can be used for arguments and comments
        post_id = request.GET.get('comment_id')
        reportedComment = Comment.objects.get(id = post_id)
        form = ReportForm(initial = {'post_id': post_id})
        context = {
            'reportedComment': reportedComment,
            'form': form
            }
    return render(request, 'main/report_comment.html', context)

def clear_comment_report(request):
    current_user = request.user
    if current_user.is_staff:
        comment_id = request.GET.get('comment_id')
        reportedComment = Comment.objects.get(id = comment_id)
        reportedComment.isReported = False
        reportedComment.reasonForBeingReported = ''
        reportedComment.save()
        return redirect('view_reported_comments')
    else:
        return render(request, 'main/staff_only.html')


def clear_argument_report(request):
    current_user = request.user
    if current_user.is_staff:
        argument_id = request.GET.get('argument_id')
        reportedArgument = Argument.objects.get(id = argument_id)
        reportedArgument.isReported = False
        reportedArgument.reasonForBeingReported = ''
        reportedArgument.save()
        return redirect('view_reported_arguments')
    else:
        return render(request, 'main/staff_only.html')


def delete_comment(request):
    current_user = request.user
    if current_user.is_staff:
        comment_id = request.GET.get('comment_id')
        reportedComment = Comment.objects.get(id = comment_id)
        reportedComment.isActive = False
        reportedComment.save()
        return redirect('view_reported_comments')
    else:
        return render(request, 'main/staff_only.html')

def delete_argument(request):
    current_user = request.user
    if current_user.is_staff:
        argument_id = request.GET.get('argument_id')
        reportedArgument = Argument.objects.get(id = argument_id)
        reportedArgument.isActive = False
        reportedArgument.save()
        return redirect('view_reported_arguments')
    else:
        return render(request, 'main/staff_only.html')

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
    current_user = request.user
    if request.method == 'POST':
        if current_user.is_staff:
            form = JoinFormMod(request.POST)
            if form.is_valid():
                role = form.cleaned_data['role']
                side = form.cleaned_data['side']
                profile = UserInfo.objects.get(user = current_user)
                profile.current_role = role
                if role == 'D' or role == 'M':
                    profile.current_side = side
                else:
                    profile.current_side = 'S'
                profile.save()
                return redirect('home')
        else:
            form = JoinForm(request.POST)
            if form.is_valid():
                role = form.cleaned_data['role']
                side = form.cleaned_data['side']
                profile = UserInfo.objects.get(user = current_user)
                profile.current_role = role
                if role == 'D':
                    profile.current_side = side
                else:
                    profile.current_side = 'S'
                profile.save()
                return redirect('home')
    if current_user.is_staff:
        form = JoinFormMod()
    else:
        form = JoinForm()
    current_debate = DailyDebate.objects.get(is_current_debate = True) #fetches debate marked current
    context = {
        'debate': current_debate,
        'form' : form
    }
    return render(request, 'main/join.html', context)

def set_debate(request):
    current_user = request.user
    if request.method == 'POST' and current_user.is_staff:
        form = TopicForm(request.POST)
        if form.is_valid():
            #make old current debate inactive
            current_debate = DailyDebate.objects.filter(is_current_debate = True)
            for item in current_debate:
                item.is_current_debate = False
                item.save()
            #set new debate
            new_topic = form.cleaned_data['topic']
            debate = DailyDebate(topic = new_topic, is_current_debate = True)
            debate.save()
            return render(request, 'main/add_debate_success.html')
    elif current_user.is_staff:
        return render(request, 'main/set_debate.html', {'form': TopicForm()})
    else:
        return render(request, 'main/staff_only.html')

def confirm_comment(request):
    if request.method == 'POST':
        form = MakeCommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            profile = UserInfo.objects.get(user = current_user)

            temp_content = form.cleaned_data['content']
            post_id = form.cleaned_data['post_id']
            temp_source = form.cleaned_data['source']
            temp_author = current_user
            temp_side = profile.current_side
            temp_parent_post = Argument.objects.get(id = post_id)
            current_debate = DailyDebate.objects.filter(is_current_debate = True)[0]

            new_comment = Comment(author = temp_author, side = temp_side, content = temp_content, parent_debate = current_debate, parent_post = temp_parent_post)
            new_comment.save()
            return redirect('debate')
    else:
        post_id = request.GET.get('post_id')
        parent_post = Argument.objects.get(id = post_id)
        form = MakeCommentForm(initial = {'post_id': post_id})
        context = {
            'post_id': post_id,
            'parent_post': parent_post,
            'form': form
            }
    return render(request, 'main/confirm_comment.html', context)

def score_post(request):
    if request.method == 'POST':
        form = ScoreArgumentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            post_id = form.cleaned_data['post_id']

            post_temp = Argument.objects.get(id = post_id)
            understands_topic_temp = form.cleaned_data['understands_topic']
            respectful_temp = form.cleaned_data['respectful']
            logical_temp = form.cleaned_data['logical']
            accurate_info_temp = form.cleaned_data['accurate_info']
            convincing_temp = form.cleaned_data['convincing']
            total_temp = int(understands_topic_temp) + int(respectful_temp) + int(logical_temp) + int(accurate_info_temp) + int(convincing_temp)

            new_score = Rubric(total = total_temp, post = post_temp, grader = current_user, understand_topic = understands_topic_temp, respectful = respectful_temp, logical = logical_temp, accurate_info = accurate_info_temp, convincing = convincing_temp)
            new_score.save()
            redirect('spectate')
        return redirect('spectate')
    else:
        post_id = request.GET.get('post_id')
        selected_argument = Argument.objects.get(id = post_id)
        form = ScoreArgumentForm(initial = {'post_id': post_id})
        context = {
            'selected_argument': selected_argument,
            'form': form
            }
        return render(request, 'main/score_argument.html', context)
