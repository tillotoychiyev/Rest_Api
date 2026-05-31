from rest_framework.views import APIView
from .models import Course, Student
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import CourseSerializer, StudentSerializer
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
            return Response({"message": "Method PUT not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request:Request, pk: int=None):
        if pk:
            course = get_object_or_404(Course, pk=pk)
            course.delete()
            return Response({"message":"Course delete successful"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Method DELETE not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



class StudentAPIView(APIView):
    def get(self, request:Request, pk:int = None):
        if not pk:
            students = Student.objects.all()
            return Response(StudentSerializer(students, many=True).data)
        else:
            student = Student.objects.get(pk=pk)
            return Response(StudentSerializer(student).data)

    def post(self, request: Request, pk=None):
        if pk:
            return Response({"message": "Method POST not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)

        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        course = get_object_or_404(Course, pk=serializer.validated_data["course"])
        student = Student.objects.create(
            full_name=serializer.validated_data["full_name"],
            age=serializer.validated_data["age"],
            address=serializer.validated_data["address"],
            hobby=serializer.validated_data.get("hobby"),
            course=course
        )

        return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)

    def put(self, request:Request, pk:int=None):
        if pk:
            student = get_object_or_404(Student, pk=pk)
            serializer = StudentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            student.full_name = serializer.validated_data.get("full_name", student.full_name)
            student.age = serializer.validated_data.get("age", student.age)
            student.address = serializer.validated_data.get("address", student.address)
            student.hobby = serializer.validated_data.get("hobby", student.hobby)
            course = get_object_or_404(Course, pk=serializer.validated_data["course"])
            student.course = course
            student.save()
            return Response(StudentSerializer(student).data)
        else:
            return Response({"message": "Method PUT not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request:Request, pk: int=None):
        if pk:
            student = get_object_or_404(Student, pk=pk)
            student.delete()
            return Response({"message":"Student delete successful"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Method DELETE not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
