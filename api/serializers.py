from rest_framework import serializers
from .models import Student, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    course_write = serializers.ChoiceField(
        choices=Course.objects.all(),
        write_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        course_write = validated_data.pop("course_write")
        student = Student.objects.create(course=course_write, **validated_data)
        student.save()
        return student

    def update(self, instance, validated_data):
        course = validated_data.pop("course_write", None)

        if course is not None:
            instance.course = course

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['image']