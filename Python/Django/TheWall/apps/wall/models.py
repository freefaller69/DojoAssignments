# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAILREG = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,20}$')

# Create your models here.
class UserManager(models.Manager):
    def check_create(self, data):
        errors = []
        if len(data['firstName']) < 2:
            errors.append(['firstName', "First Name must be at least two characters in length."])
        if len(data['lastName']) < 2:
            errors.append(['lastName', "Last Name must be at least two characters in length."])
        if not re.match(EMAILREG, data['email']):
            errors.append(['email', "Email must be a valid address."])
        if not re.match(PASSWORD_REGEX, data['new_pwd']):
            errors.append(['pwd', "Password must be between 8 and 20 characters in length and  include at least 1 uppercase letter, 1 lowercase letter, and 1 number."])
        elif (data['new_pwd'] != data['pwdConfirm']):
            errors.append(['pwd', "Password confirmation does not match.  Please reenter."])
        mail_check = User.objects.filter(email=data['email'])
        if mail_check:
            errors.append(['email', "Registration data error.  Please review and re-enter."])
        if errors:
            return [False, errors]
        else:
            newUser = User(first_name=data['firstName'], last_name=data['lastName'], email=data['email'], pw_hash=data['new_pwd'])
            newUser.save()
            return [True, newUser]

    def check_login(request, data):
        errors= []
        userAuth = User.objects.filter(email=data['login_email'])
        if userAuth:
            user = User.objects.get(email=data['login_email'])
            if data['login_email'] != user.email or data['login_pwd'] != user.pw_hash:
                errors.append(['login', "Invalid username or password"])
        else:
            errors.append(['login', "Invalid username or password"])
        if errors:
            return [False, errors]
        else:
            return [True, user]

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email

class Message(models.Model):
    message = models.TextField(max_length=1000)
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    message_id = models.ForeignKey(Message)
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
