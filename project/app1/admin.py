# app1/admin.py
from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Account)
admin.site.register(Account_cs)