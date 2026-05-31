from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(default=10)
    address = models.CharField(max_length=50)
    hobby = models.CharField(max_length=255, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name