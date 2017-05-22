# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
import datetime
import pytz

# Create your views here.
def index(request):
    # check for session and assign if not present
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['actions'] = []
    return render(request, "game/index.html")

def process(request):
    if request.method == 'POST':
        choice = request.POST['action']
        # set location gold ranges
        if choice == 'farm':
            start = 10
            stop = 21
        elif choice == 'cave':
            start = 5
            stop = 11
        elif choice == 'house':
            start = 2
            stop = 6
        elif choice == 'casino':
            start = -50
            stop = 51
        # process gold for location selected
        goldThisRound = random.randrange(start, stop)
        request.session['gold'] += goldThisRound
        place = choice

        today = datetime.datetime.today().strftime('%Y/%m/%d %I:%M:%S %p')
        dt_UTC = datetime.datetime.now(tz=pytz.UTC)
        dt_mtn = dt.astimezone(pytz.timezone('US/Mountain'))
        print "*"*100
        print today
        print dt_UTC
        print dt_mtn
        print "*"*100
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
