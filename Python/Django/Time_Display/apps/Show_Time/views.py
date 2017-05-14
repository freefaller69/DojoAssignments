# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.utils import timezone

# Create your views here.
def index(request):
    timeDate = {
    "ctime":timezone.now(),
    }
    return render(request, "Show_Time/index.html", timeDate)
