from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
# Create your views here.

stack =[{"id":"python", "name":"python"}, {"id":"django", "name":"django"}, {"id":"javascript", "name":"javascript"},{"id":"PHP", "name":"PHP"}]
def home(request):
    return render(request, "landing/landing.html", {
        "name": "Antoni",
        "age":27,
        "date": date.today(),
        "stack": stack
    })
    
    
def stack_detail(request, tool):
    return HttpResponse(f"You are looking for {tool} stack details!")