from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from app1.models import Account_cs
# Create your views here.
def main(requests):
    _all=Account_cs.objects.all()[0]
    print(_all.username)
    return HttpResponse(str(_all.username))