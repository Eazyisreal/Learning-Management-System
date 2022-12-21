from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from .serializers import TeacherSerializer, StudentSerializer , CourseCategorySerializer, CourseSerializer
from . import models



class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    
    
class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    
class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    
    
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    
    

class CourseCategoryList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = CourseCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    
    
class CourseCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = CourseCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    

class CourseList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    
    
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]