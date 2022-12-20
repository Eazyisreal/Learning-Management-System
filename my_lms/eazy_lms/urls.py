from django.urls import path
from . import views


urlpatterns =[
    path('teacher/', views.TeacherList.as_view()),
]