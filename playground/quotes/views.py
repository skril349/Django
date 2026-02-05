from email.policy import HTTP
# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return HttpResponse("Hello from the quotes app!")

days_of_week = {
    "monday": "Monday quote",
    "tuesday": "Tuesday quote",
    "wednesday": "Wednesday quote",
    "thursday": "Thursday quote",
    "friday": "Friday quote",
    "saturday": "Saturday quote",
    "sunday": "Sunday quote",
}

def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day < 1 or day > len(days):
        return HttpResponseNotFound("<h1>Invalid day number!</h1>")
    redirect_day = days[day - 1]
    redirect_path = reverse("week", args=[redirect_day])
    return HttpResponseRedirect(redirect_path)


def week(request, day):
    quote_text = None
    if day.lower() in days_of_week:
        quote_text = days_of_week[day.lower()]
    else:
        return HttpResponseNotFound("Invalid day!")
    return HttpResponse(f"Happy {day.capitalize()}! {quote_text}")

def index(request):
    list_items = ""
    for day in days_of_week:
        day_path = reverse("week", args=[day])
        list_items += f"<li><a href='{day_path}'>{day.capitalize()}</a></li>"
    response_html = f"<ul>{list_items}</ul>"
    return HttpResponse(response_html)