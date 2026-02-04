from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello from the quotes app!")

def week(request, day):
    return HttpResponse(f"Happy {day.capitalize()}!")