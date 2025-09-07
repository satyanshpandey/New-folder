from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import StudentRegionNorth, StudentRegionSouth  ,Profile, Student, Teacher, Course, Subject
from .serializers import StudentRegionNorthSerializer, StudentRegionSouthSerializer , ProfileSerializer, StudentSerializer, TeacherSerializer, CourseSerializer, SubjectSerializer
from rest_framework import viewsets 
# Simple function-based view
from rest_framework.response import Response
from rest_framework.decorators import api_view

def home(request):   
    return HttpResponse("Welcome to the School Management System API")  

# ViewSets for CRUD operations
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class StudentRegionNorthViewSet(viewsets.ModelViewSet):
    queryset = StudentRegionNorth.objects.all()
    serializer_class = StudentRegionNorthSerializer

class StudentRegionSouthViewSet(viewsets.ModelViewSet):
    queryset = StudentRegionSouth.objects.all()
    serializer_class = StudentRegionSouthSerializer         
    
    
