# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from ..logreg.models import UserDB

from datetime import datetime, tzinfo
import pytz

# Create your models here.
class SecretDataManager(models.Manager):
    def new_secret_input(self, data, id):
        errors= []
        user_id = UserDB.objects.get(id=id)
        if len(data['secret_input']) < 2:
            errors.append(['secret', "Secrets have a minimum length of two characters."])
        if errors:
            return [False, errors]
        else:
            newSecret = Secret(secret=data['secret_input'], user_id=user_id)
            newSecret.save()
            return [True]



class Secret(models.Model):
    secret = models.TextField(max_length=1000)
    user_id = models.ForeignKey('logreg.UserDB', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SecretDataManager()

    def __str__(self):
        return 'ID: %s | Secret: %s | User_ID: %s | CreatedAt: %s' % (self.id, self.secret, self.user_id, self.created_at)

class LikeManager(models.Manager):
    def like_secret(self, user_id, secret_id):
        Like.objects.create(user_id=UserDB.objects.get(id=user_id), secret_id=Secret.objects.get(id=secret_id))

    def get_likes(self):
        return Likes.objects.all()

class Like(models.Model):
    secret_id = models.ForeignKey(Secret, related_name='secret_likes', on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserDB, related_name='user_likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = LikeManager()

    def __str__(self):
        return 'ID: %s | Secret ID: %s | User_ID: %s | CreatedAt: %s' % (self.id, self.secret_id, self.user_id, self.created_at)
