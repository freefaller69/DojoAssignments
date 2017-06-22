# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Book, Author, Review

# Create your views here.
def index(request):
    return render(request, "bookReviews/index.html")

def book(request, id):
    book_check = Book.objects.filter(id=id)
    if book_check:
        context = {
            "books": Book.objects.get(id=id),
            "author": Author.objects.all(),
            "reviews": Review.objects.all(),
        }
        return render(request, "bookReviews/book.html", context)
    else:
        return render(request, "bookReviews/books.html")

def books(request):
    context = {
        "books": Book.objects.all().order_by('title'),
        "reviews": Review.objects.all(),
    }
    return render(request, "bookReviews/books.html", context)

def add(request):
    context = {
        "authors": Author.objects.all().order_by('name'),
    }
    return render(request, "bookReviews/add.html", context)

def add_book(request):
    if request.method == "POST":
        response = Book.objects.create_book(request.POST)
    if not response[0]:
        for error in response[1]:
            messages.error(request, error[1])
        return redirect('bookReviews:add')
    else:
        return redirect('bookReviews:books')
    return redirect('bookReviews:books')
