# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseDataManager(models.Manager):
    def check_create(self, data):
        errors = []
        if len(data['name']) < 2:
            errors.append(['name', "Course name must be at least two characters in length."])
        if len(data['description']) < 2:
            errors.append(['description', "Course description must be at least two characters in length."])
        if errors:
            return [False, errors]
        else:
            newCourse = Course(name=data['name'], description=data['description'])
            print "x"*100
            print "New Course"
            print newCourse
            print "x"*100
            newCourse.save()
            print "x"*100
            print "completed check"
            print "x"*100
            return [True, newCourse]

class Course(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseDataManager()

    def __str__(self):
        return 'ID: %s | Name: %s | Description: %s | CreatedAt: %s' % (self.id, self.name, self.description, self.created_at)
