
from django.urls import path
from . import views


urlpatterns = [
    path('hola-mundo/', views.index, name='index'),
]