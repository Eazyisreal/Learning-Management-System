# import the path function from django.urls and include from my_lms/urls.py
from django.urls import path, include
# import views from eazy_lms/views.py
from . import views


urlpatterns =[
    #  urls path for TeacherList and TeacherDetail
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    # urls path for StudentList and StudentDetail
    path('teacher/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    # urls path for CourseCategoryList and CourseCategoryDetail
    path('coursecategory/', views.CourseCategoryList.as_view()),
    path('coursecategory/<int:pk>/', views.CourseCategoryDetail.as_view()),
    # urls path for CourseList and CourseDetail
    path('course/', views.CourseList.as_view()),
    path('course/<int:pk>/', views.CourseDetail.as_view()),
    # urls path for authentication
    path('api-auth/', include('rest_framework.urls')),
]