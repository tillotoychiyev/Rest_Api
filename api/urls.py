from django.urls import path
from .views import CourseAPIView, CourseRetrieveAPIView, StudentAPIView, StudentRetrieveAPIView

urlpatterns = [
    path('courses', CourseAPIView.as_view()),
    path('courses/<int:pk>/', CourseRetrieveAPIView.as_view()),

    path('students', StudentAPIView.as_view()),
    path('students/course/<int:course_id>/', StudentAPIView.as_view()),
    path('students/ball/<int:ball>/', StudentAPIView.as_view()),
    path('students/<int:student_id>/', StudentRetrieveAPIView.as_view()),
]