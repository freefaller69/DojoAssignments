# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "turtle_power/index.html")

def show_ninja(request, color):
    # if ninja button is pressed, no color
    if color == "":
        name = "all"
        context = {
            "turtle":name,
        }
    # if color belongs to color group
    elif color.lower() in ['blue', 'orange', 'red', 'purple']:
        if color.lower() == "blue":
            name = "leonardo"
        if color.lower() == "orange":
            name = "michelangelo"
        if color.lower() == "red":
            name = "raphael"
        if color.lower() == "purple":
            name = "donatello"
        context = {
            "turtle":name,
            "caption":name.upper(),
        }
    # if anything outside of color group entered into url
    else:
        name = "notapril"
        context = {
            "turtle":name,
        }
    return render(request, "turtle_power/index.html", context)
