# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
import string

# Create your views here.
def index(request):
    generator = {
    "rwg":''.join(random.choice(string.ascii_uppercase) for x in range(15))
    }
    request.session['count'] += 1
    return render(request, "rwg/index.html", generator)

def counter(request):
    pass
