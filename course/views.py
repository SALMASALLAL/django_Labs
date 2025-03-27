from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer

def add_course(req):
    if req.method == 'POST':
        name = req.POST["name"]
        description = req.POST["description"]
        duration = req.POST["duration"]
        Course.objects.create(name=name,description=description,duration=duration)
        return redirect("course_list")
    return render(req, 'course/add_course.html')

def update_course(req, id):
    course = Course.objects.get(id=id)
    if not course:
        return redirect("course_list")
    
    if req.method == 'POST':
        course.name = req.POST["name"]
        course.description = req.POST["description"]
        course.duration = req.POST["duration"]
        course.save()
        return redirect("course_list")
    
    return render(req, 'course/update_course.html', {'course': course})

def course_list(req):
    courses=Course.objects.all()
    return render(req, 'course/course_list.html', {'courses': courses})

def delete_course(req, id):
    Course.objects.get(id=id).delete()
    return redirect("course_list")



class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer