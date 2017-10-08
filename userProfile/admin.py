# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import User, Album, Song

admin.site.register(Album)
admin.site.register(User)
admin.site.register(Song)