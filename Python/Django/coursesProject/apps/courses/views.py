# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Course

from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all().order_by('name'),
    }
    return render(request, 'courses/index.html', context)

def add_course(request):
    if request.method == "POST":
        response = Course.objects.check_create(request.POST)
    if not response[0]:
        for error in response[1]:
            messages.error(request, error[1])
    return redirect('courses:index')

def destroy(request, id):
    context = {
        "course": Course.objects.get(id=id),
    }
    print context
    return render(request, 'courses/destroy.html', context)

def course_delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('courses:index')
