
from django.urls import path
from . import views


urlpatterns = [
    path('monday', views.monday, name='monday'),
    path('tuesday', views.tuesday, name='tuesday'),
    path('wednesday', views.wednesday, name='wednesday'),
    path('thursday', views.thursday, name='thursday'),
    path('friday', views.friday, name='friday'),
    path('saturday', views.saturday, name='saturday'),
    path('sunday', views.sunday, name='sunday'),


]