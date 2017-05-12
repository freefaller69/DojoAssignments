# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

users = [

]

def index(request):
    print "ninja " * 5
    context = {
        "users": users
    }
    return render(request, "hello/index.html")
# Create your views here.
def show(request, id):
    print(request.method)
    return render(request, "hello/show_users.html")

def projects(request):
    return render(request, "projects/index.html")

def about(request):
    return render(request, "about/index.html")

def testimonials(request):
    return render(request, "testimonials/index.html")
