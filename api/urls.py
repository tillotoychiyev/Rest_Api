from django.urls import path
from .views import CourseAPIView, StudentAPIView

urlpatterns = [
    path('courses', CourseAPIView.as_view()),
    path('courses/<int:pk>/', CourseAPIView.as_view()),
    path('students', StudentAPIView.as_view()),
    path('students/<int:pk>/', StudentAPIView.as_view()),
]