# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserDB
import re
EMAILREG = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your views here.
def entrance(request):
    if request.method == "POST":
        if request.POST["gate"] == "register":
            response = UserDB.objects.check_create(request.POST)
        elif request.POST["gate"] == "login":
            response = UserDB.objects.check_login(request.POST)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
            return redirect('secrets:index')
        else:
            request.session['user'] = {
            "id": response[1].id,
            "first_name": response[1].first_name,
            "last_name": response[1].last_name,
            }
            return redirect('secrets:secrets')
    return redirect('secrets:index')

def user_update(request):
    user_id = str(request.session['user']['id'])
    if request.method == "POST":
        if request.POST["update_option"] == "profile":
            response = UserDB.objects.check_update(request.POST, request.session['user']['id'])
        if request.POST["update_option"] == "password":
            response = UserDB.objects.check_password(request.POST, request.session['user']['id'])
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
            return redirect('/'+user_id)
    return redirect('/'+user_id)

def user_delete(request):
    user_id = request.session['user']['id']
    UserDB.objects.filter(id=user_id).delete()
    return redirect('logreg:logout')

def logout(request):
    request.session.clear()
    return redirect('secrets:index')
