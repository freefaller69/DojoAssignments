# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "landscapePhoto/index.html")

def result(request, number):
    number = int(number)
    print "*"*100
    print number
    print type(number)
    print "*"*100
    if number in range (1,51):
        if number <= 10:
            choice = "snow"
        elif number <= 20:
            choice = "desert"
        elif number <= 30:
            choice = "forest"
        elif number <= 40:
            choice = "vineyard"
        elif number <= 50:
            choice = "tropical"
        context = {
            "photo":choice,
        }
    else:
        return render(request, "landscapePhoto/index.html")
    print "$"*100
    print context
    print "$"*100
    return render(request, "landscapePhoto/result.html", context)
