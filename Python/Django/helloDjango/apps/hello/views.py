# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    print "ninja " * 5
    return render(request, "hello/index.html")
# Create your views here.
def show(request):
    print(request.method)
    return render(request, "hello/show_users.html")
