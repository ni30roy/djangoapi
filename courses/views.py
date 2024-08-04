from django.shortcuts import render
from rest_framework import viewsets
from courses.models import Courses
from courses.serializers import CourseSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
