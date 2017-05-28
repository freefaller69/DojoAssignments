# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UsernameManager(models.Manager):
    def check_create(self, data):
        errors = []
        if len(data['username']) < 8 or len(data['username']) > 16:
            errors.append(['username', "Username is not valid."])
        if errors:
            return [False, errors]
        else:
            username_check = Username.objects.filter(username=data['username'])
            if username_check:
                errors.append(['username_check', "Username is not valid."])
                return [False, errors]
            newName = Username(username=data['username'])
            newName.save()
            return [True, newName]

class Username(models.Model):
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsernameManager()

    def __str__(self):
        return 'ID: %s | Username: %s | CreatedAt: %s' % (self.id, self.username, self.created_at)
