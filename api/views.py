from rest_framework.views import APIView
from django.forms.models import model_to_dict

from .models import Course, Student
from rest_framework.request import Request
from rest_framework.response import Response

class CourseAPIView(APIView):
    def get(self, request:Request, pk:int = None):
        courses = Course.objects.all()
        if not pk:
            course_list = []
            for course in courses:
                course_list.append(
                    {
                        'id':course.pk,
                        'name':course.name
                    }
                )
            return Response(course_list)
        else:
            course = Course.objects.get(pk=pk)
            return Response(model_to_dict(course))

class StudentAPIView(APIView):
    def get(self, request:Request, pk:int = None):
        students = Student.objects.all()
        if not pk:
            student_list = []
            for student in students:
                student_list.append(
                    {
                        'id':student.pk,
                        'name':student.full_name
                    }
                )
            return Response(student_list)
        else:
            student = Student.objects.get(pk=pk)
            return Response(model_to_dict(student))