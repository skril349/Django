
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:day>", views.days_week_with_number, name="day_number"),
    path("<str:day>", views.week, name="week"),
]