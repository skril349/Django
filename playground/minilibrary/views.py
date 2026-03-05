from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def index(request):
    try:
        return render(request, "minilibrary/minilibrary.html", {
            "text": "Bienvenido a la mini biblioteca",
            "name": "Mini Biblioteca"
        }
        )
    except Exception as e:
        return HttpResponseNotFound(f"Error: {str(e)}")