from django.shortcuts import render

# Create your views here.

def course_list(request):
    courses = [
        {
            'course_title': 'Python for Beginners',
            'description': 'Learn Python from scratch with this comprehensive course.',
            'rating': 4.5,
            'level': 'Beginner',
            'course_image': 'images/curso_1.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/32.jpg',
            'instructor': 'John Doe',
            'id':1
        },
        {
            'course_title': 'Web Development with Django',
            'description': 'Build powerful web applications using Django framework.',
            'rating': 4.7,
            'level': 'Intermediate',
            'course_image': 'images/curso_2.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/20.jpg',
            'instructor': 'Jane Smith',
            'id':2
            
        },
        {
            'course_title': 'Data Science with Python',
            'description': 'Master data analysis and visualization with Python.',
            'rating': 4.8,
            'level': 'Advanced',
            'course_image': 'images/curso_3.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/45.jpg',
            'instructor': 'Alice Johnson',
            'id':3
        }
    ]
    return render(request, 'courses/courses.html', {'courses': courses})

def course_detail(request): 
    course = {
        "course_title": 'Python for Beginners',
        "course_link":"course_lessons",
        "course_image": 'images/curso_2.jpg',
        "info_course": {
            "lessons": 79,
            "duration": 8,
            "instructor": "Toni Vives"
        },
        "course_content":[
            {
                "id":1,
                "name":"Introduction to Python",
                "lessons":[
                    {
                        "name":"What is Python?",
                        "type":"video"
                    },
                    {
                        "name":"Setting up Python",
                        "type":"article"
                    }
                ]
            }
        ]
    }
    return render(request, 'courses/course_detail.html', {'course': course})

def course_lessons(request):
    pass