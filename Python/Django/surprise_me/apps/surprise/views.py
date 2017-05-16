# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    return render(request, "surprise/index.html")

def surprise(request):
    values = ['bird', 'car', 'apple', 'cow', 'mountain', 'tree', 'farm', 'bunny', 'coffee', 'egg' ]
    surprises = []
    if int(request.POST['num']) > len(values):
        num = len(values)
    else:
        num = int(request.POST['num'])
    for items in range(1,num+1):
        if len(values) > 0:
            index = random.randint(0,len(values)-1)
            item = values.pop(index)
            surprises.append(item)
    context = {
        "surprises":surprises
    }
    return render(request, "surprise/results.html", context)
