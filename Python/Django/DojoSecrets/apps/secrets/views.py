# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render, redirect
from ..logreg.models import UserDB
from .models import Secret, Like

# Create your views here.
def index(request):
    return render(request, "secrets/index.html")

def secrets(request):
    context = {
        "secrets": Secret.objects.all().order_by('id').reverse()[:10],
        "current_user": UserDB.objects.get(id=request.session['user']['id'])
    }
    return render(request, "secrets/secrets.html", context)

def post_secret(request):
    if request.method == "POST":
        response = Secret.objects.new_secret_input(request.POST, request.session['user']['id'])
    return redirect('secrets:secrets')

def secret_like(request, secret_id):
    Like.objects.like_secret(request.session['user']['id'], secret_id)
    return redirect('secrets:secrets')

def user(request, id):
    user_check = UserDB.objects.filter(id=id)
    if user_check:
        context = {
            "user": UserDB.objects.get(id=id),
        }
        return render(request, "secrets/user.html", context)
    else:
        return redirect('secrets:all_users')

def all_users(request):
    context = {
        "all": UserDB.objects.all(),
    }
    return render(request, "secrets/allusers.html", context)

def delete_secret(request, secret_id):
    Secret.objects.filter(id=secret_id).delete()
    return redirect('secrets:secrets')
