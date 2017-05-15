# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
    # check for session and assign if not present
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'actions' not in request.session:
        request.session['actions'] = []
    return render(request, "game/index.html")

def process(request):
    if request.method == 'POST':
        choice = request.POST['action']
        # set location gold ranges
        if choice == 'farm':
            start = 10
            stop = 21
        if choice == 'cave':
            start = 5
            stop = 11
        if choice == 'house':
            start = 2
            stop = 6
        if choice == 'casino':
            start = -50
            stop = 51
        # process gold for location selected
        goldThisRound = random.randrange(start, stop)
        request.session['gold'] += goldThisRound
        request.session['place'] = choice
        place = choice

        today = datetime.datetime.today().strftime('%Y/%m/%d %I:%M:%S %p')
        action = {
            "goldThisRound": goldThisRound,
            "place": choice,
            "stamp": today
        }
        request.session['actions'].append(action)

    return redirect('/')

def reset_session(request):
    request.session.clear()
    return redirect('/')
