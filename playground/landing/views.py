from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
# Create your views here.

stack = ["python", "django", "javascript","PHP"]
def home(request):
    return render(request, "landing/landing.html", {
        "name": "Antoni",
        "age":27,
        "date": date.today(),
        "stack": stack
    })