from django.urls import path, include
from . import views


urlpatterns =[
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    path('coursecategory/<int:pk>/', views.CourseCategoryDetail.as_view()),
    path('course/<int:pk>/', views.CourseDetail.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]