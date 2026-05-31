from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=50)
    hobby = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    course = serializers.IntegerField(source="course.id")