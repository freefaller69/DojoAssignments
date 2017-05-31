# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt, re
EMAILREG = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z)(?=.*[\W_]).{8,}$')
# Create your models here.
class UserDataManager(models.Manager):
    def check_create(self, data):
        errors = []
        if len(data['firstName']) < 2:
            errors.append(['firstName', "First Name must be at least two characters in length."])
        if len(data['lastName']) < 2:
            errors.append(['lastName', "Last Name must be at least two characters in length."])
        if not re.match(EMAILREG, data['email']):
            errors.append(['email', "Email must be a valid address."])
        if not re.match(PASSWORD_REGEX, data['password']):
            errors.append(['password', "Password must be at least 8 characters in length and  include 1 uppercase letter, 1 lowercase letter, and 1 number."])
        if (data['password'] != data['pwdConfirm']):
            errors.append(['pwdConfirm', "Password confirmation does not match.  Please reenter."])
        if errors:
            return [False, errors]
        else:
            mail_check = UserDB.objects.filter(email=data['email'])
            if mail_check:
                errors.append(['mail_check', "Unable to register, please use alternate information."])
                return [False, errors]
            newUser = UserDB(first_name=data['firstName'], last_name=data['lastName'], email=data['email'])
            hashed_pass = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            newUser.pw_hash = hashed_pass
            newUser.save()
            return [True, newUser]

    def check_update(self, data, id):
        errors = []
        current_user = UserDB.objects.get(id=id)
        if data['firstName'] != "":
            current_user.first_name = data['firstName']
        if data['lastName'] != "":
            current_user.last_name = data['lastName']
        if data['email'] != "":
            current_user.email = data['email']
            mail_check = UserDB.objects.filter(email=data['email'])
            if mail_check:
                errors.append(['mail_check', "Invalid email, please use alternate information."])
            elif not re.match(EMAILREG, data['email']):
                errors.append(['email', "Email must be a valid address."])
        if errors:
            return [False, errors]
        current_user.save()
        return [True]

    def check_password(self, data, id):
        errors = []
        user_id = UserDB.objects.get(id=id)
        if data['password'] != "":
            if not re.match(PASSWORD_REGEX, data['password']):
                errors.append(['password', "Password must be at least 8 characters in length and  include 1 uppercase letter, 1 lowercase letter, and 1 number."])
            if (data['password'] != data['pwdConfirm']):
                errors.append(['pwdConfirm', "Password confirmation does not match.  Please reenter."])
            if errors:
                return [False, errors]
            pw_hash = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            UserDB.objects.filter(id=id).update(pw_hash=pw_hash)
        return [True]

    def check_login(self, data):
        errors= []
        current_user = UserDB.objects.filter(email=data['email'])
        if not current_user:
            errors.append(['account', "Invalid username/password combination."])
        elif not bcrypt.checkpw(data['password'].encode(), current_user[0].pw_hash.encode()):
            errors.append(['account', "Invalid username/password combination."])
        if errors:
            return [False, errors]
        else:
            return [True, current_user[0]]

class UserDB(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserDataManager()

    def __str__(self):
        return 'ID: %s | Name: %s %s | Email: %s | Created: %s | Updated: %s' % (self.id, self.first_name, self.last_name, self.email, self.created_at, self.updated_at)
