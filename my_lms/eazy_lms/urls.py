from django.urls import path, include
from . import views


urlpatterns =[
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]