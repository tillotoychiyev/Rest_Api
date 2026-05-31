from rest_framework.views import APIView
from django.forms.models import model_to_dict

from .models import Course, Student
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import CourseSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404

class CourseAPIView(APIView):
    def get(self, request:Request, pk:int = None):
        if not pk:
            courses = Course.objects.all()
            return Response(CourseSerializer(courses, many=True).data)
        else:
            course = Course.objects.get(pk=pk)
            return Response(CourseSerializer(course).data)

    def post(self, request:Request, pk=None):
        if pk:
            return Response({"message":"Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        course = Course.objects.create(**serializer.validated_data)
        return Response(CourseSerializer(course).data)

    def put(self, request:Request, pk:int=None):
        if pk:
            course = get_object_or_404(Course, pk=pk)
            serializer = CourseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            course.name = serializer.validated_data.get("name", course.name)
            course.save()
            return Response(CourseSerializer(course).data)
        else:
            return Response({"message": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request:Request, pk: int=None):
        if pk:
            course = get_object_or_404(Course, pk=pk)
            course.delete()
            return Response({"message":"Course delete successful"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


#
#
# class StudentAPIView(APIView):
#     def get(self, request:Request, pk:int = None):
#         students = Student.objects.all()
#         if not pk:
#             student_list = []
#             for student in students:
#                 student_list.append(
#                     {
#                         'id':student.pk,
#                         'name':student.full_name,
#                         'age':student.age,
#                         'address':student.address,
#                         'hobby':student.hobby
#                     }
#                 )
#             return Response(student_list)
#         else:
#             student = Student.objects.get(pk=pk)
#             return Response(model_to_dict(student))
#
