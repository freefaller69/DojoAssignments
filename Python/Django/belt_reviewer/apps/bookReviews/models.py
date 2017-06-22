# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class BookDataManager(models.Manager):
    def create_book(self, data, author_id, user_id):
        errors = []
        if data['bookTitle'] != "":
            title_check = Book.objects.filter(title=data['bookTitle'])
            if title_check:
                current_book = title_check
                print "CURRENT BOOK:",current_book
            else:
                print data['bookTitle']
                if data['authorList'] != "":
                    pass
                print data['authorList']
                print data['authorName']
                print data['review_input']
                print data['rating']
        return [True]

class Book(models.Model):
    title = models.CharField(max_length=150)
    author_id = models.ForeignKey('bookReviews.Author', related_name='book_author')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookDataManager()

    def __str__(self):
        return 'ID: %s | Title: %s' % (self.id, self.title)

class AuthorDataManager(models.Manager):
    def get_all_authors(self):
        return Author.objects.all()

    def create_author(self, data):
        author_check = Author.objects.filter(name=data['authorName'])
        if not author_check:
            Author.objects.create(name=data['authorName'])
        return [Author.objects.get(name=data['authorName'])]



class Author(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AuthorDataManager()

    def __str__(self):
        return 'ID: %s | Name: %s' % (self.id, self.name)

class ReviewDataManager(models.Manager):
    pass

class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.IntegerField()
    user_id = models.ForeignKey('logreg.UserDB', related_name='review_author')
    book_id = models.ForeignKey(Book, related_name='book_reviewed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ReviewDataManager()
