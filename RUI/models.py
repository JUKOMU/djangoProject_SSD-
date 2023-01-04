from django.db import models


# Create your models here.
class Lessons(models.Model):
    lesson_name = models.CharField(max_length=40)
    lesson_hour = models.CharField(max_length=30)
    lesson_week = models.CharField(max_length=40)
    lesson_date = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
    teacher = models.CharField(max_length=30)
    classroom = models.CharField(max_length=30)


class Student(models.Model):
    gender_choices = [(1, 'Male'), (0, 'Female')]
    party_member = [(1, 'is'), (0, 'not')]
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.IntegerField(choices=gender_choices)
    department = models.CharField(max_length=100)
    grade = models.IntegerField()
    class_i = models.IntegerField()
    party_member = models.IntegerField(choices=party_member)
    selected_lessons = models.CharField(max_length=100)
