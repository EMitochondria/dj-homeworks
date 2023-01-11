from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from students.models import Course
from django_testing.settings import MAX_STUDENTS_PER_COURSE


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        """Проверка, что на курсе не больше больше 20 студентов"""
        students = data['students']
        students_count = len(students)
        if students_count >= MAX_STUDENTS_PER_COURSE:
            raise ValidationError('Вы не можете добавить больше 20 студентов в курс')
        return data
