from django.db import models
from django.urls import reverse_lazy

class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название курсов')
    mentor = models.CharField(max_length=20, verbose_name='Имя ментора')
    month = models.IntegerField(default=6, verbose_name='Длительность курсов')

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО студента')
    laptop = models.CharField(max_length=20, choices=(
        ('mac', 'MacBook'),
        ('linux', 'Linux'),
        ('windows', 'Windows')
    ), verbose_name='Операционная система')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.id})



