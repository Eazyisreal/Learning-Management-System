from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TeacherSerializer
from . import models

# Create your views here.
class TeacherList(APIView):
    def get(self,request):
        teachers = models.Teacher.objects.all()
        serializer = TeacherSerializer(teachers,many= True)
        return Response(serializer.data)
        
        
        
# class Studentlist(APIView):
#     def get (self, request):
#         students = models.Student.objects.all()
#         serializer = 