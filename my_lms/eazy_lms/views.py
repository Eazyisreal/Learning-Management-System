from django.shortcuts import render
from rest_framework.response import Response
# import APIView from rest_framework
from rest_framework.views import APIView
# import generics from rest_framework
from rest_framework import generics
# import permissions from rest_framework
from rest_framework import permissions
# import individual serializers from serializers.py
from .serializers import TeacherSerializer, StudentSerializer , CourseCategorySerializer, CourseSerializer
# import individual models from models.py
from . import models


# TeacherList
class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
# TeacherDetail
    
class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
# StudentList
class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
# StudentDetail
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# CourseCategoryList 

class CourseCategoryList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = CourseCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
# CourseCategoryDetail
class CourseCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = CourseCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
# CourseList
class CourseList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
# CourseDetail
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]