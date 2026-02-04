from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello from the quotes app!")

def monday(request):
    return HttpResponse("Happy Monday!")
def tuesday(request):
    return HttpResponse("Happy Tuesday!")
def wednesday(request):
    return HttpResponse("Happy Wednesday!")
def thursday(request):
    return HttpResponse("Happy Thursday!")
def friday(request):
    return HttpResponse("Happy Friday!")
def saturday(request):
    return HttpResponse("Happy Saturday!")
def sunday(request):
    return HttpResponse("Happy Sunday!")