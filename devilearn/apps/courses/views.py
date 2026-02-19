from django.shortcuts import render

# Create your views here.

def course_list(request):
    return render(request, 'courses/courses.html')

def course_detail(request, slug):
    pass

def course_lessons(request):
    pass