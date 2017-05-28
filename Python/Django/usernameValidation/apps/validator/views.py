# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Username

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "validator/index.html")

def add_username(request):
    if request.method == "POST":
        response = Username.objects.check_create(request.POST)
    if not response[0]:
        for error in response[1]:
            messages.error(request, error[1])
        return redirect('validator:index')
    return redirect('validator:success')

def success(request):
    context = {
        "users": Username.objects.all().order_by('username'),
    }
    return render(request, "validator/success.html", context)

def destroy(request, id):
    Username.objects.get(id=id).delete()
    return redirect('validator:success')
