from .models import Course, Student
from .serializers import CourseSerializer, StudentSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class CourseAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'course_id'
    lookup_url_kwarg = 'course_id'

class CourseRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentAPIView(ListCreateAPIView):
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        if course_id:
            return Student.objects.filter(course_id=course_id)
        return Student.objects.all()

    def get_queryset(self):
        ball = self.kwargs.get("ball")
        if ball :
            return Student.objects.filter(ball=ball)
        return Student.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return StudentSerializer
        return UserSerializer

class StudentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'student_id'