from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО учителя')
    class_name = models.CharField(max_length=20, choices=(
        ('a_class', 'a_class'),
        ('b_class', 'b_class'),
        ('c_class', 'c_class')
    ), verbose_name='Название класса')

    def __str__(self):
        return self.name


class Pupil(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО школьника')
    birth_date = models.DateField(verbose_name='Дата рождения школьника')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



