from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def index(request):
    return HttpResponse("Hello from the quotes app!")

def week(request, day):
    quote_text = None
    if day == "monday":
        quote_text = "Monday quote"
    elif day == "tuesday":
        quote_text = "Tuesday quote"
    elif day == "wednesday":
        quote_text = "Wednesday quote"
    elif day == "thursday":
        quote_text = "Thursday quote"
    elif day == "friday":
        quote_text = "Friday quote"
    elif day == "saturday":
        quote_text = "Saturday quote"
    elif day == "sunday":
        quote_text = "Sunday quote"
    else:
        return HttpResponseNotFound("Invalid day!")
    return HttpResponse(f"Happy {day.capitalize()}! {quote_text}")