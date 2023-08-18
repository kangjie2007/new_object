from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin

# Create your views here.
def main(requests):
    return HttpResponse("app-1-main")