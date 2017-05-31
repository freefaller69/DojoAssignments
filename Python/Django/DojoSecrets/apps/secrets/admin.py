# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Secret, Like

# Register your models here.
admin.site.register(Secret)
admin.site.register(Like)
