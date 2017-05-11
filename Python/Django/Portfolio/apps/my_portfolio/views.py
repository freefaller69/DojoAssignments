# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print "woohoo " * 3
    return render(request, "my_portfolio/index.html")

def testimonials(request):
    print(request.method)
    return render(request, "my_portfolio/testimonials.html")

def projects(request):
    print(request.method)
    return render(request, "my_portfolio/projects.html")

def about(request):
    print(request.method)
    return render(request, "my_portfolio/about.html")
