# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "turtle_power/index.html")

def show_ninja(request, color):
    # if ninja button is pressed, no color
    color = color.lower()
    turtles = {
        "blue": ['leonardo', 'turtle_power/img/leonardo.jpg'],
        "orange": ['michelangelo', 'turtle_power/img/michelangelo.jpg'],
        "red": ['raphael', 'turtle_power/img/raphael.jpg'],
        "purple": ['donatello', 'turtle_power/img/donatello.jpg'],
    }
    context = {
        "turtles": []
    }
    if color == "":
        name = "all"
        for turtle in turtles:
            context['turtles'].append(turtles[turtle])
    # if color belongs to color group
    elif color in turtles:
        context['turtles'].append(turtles[color])
    else:
        context['turtles'].append(['april', 'turtle_power/img/notapril.jpg'])
    # if anything outside of color group entered into url
    return render(request, "turtle_power/index.html", context)
