from django import forms

from .models import Teacher, Pupil

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'