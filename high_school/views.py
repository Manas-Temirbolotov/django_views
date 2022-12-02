from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Teacher, Pupil
from .forms import TeacherForm


def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'teacher_list.html', context)

def teacher_create(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('teacher_list'))
    context = {
        'form': form
    }
    return render(request, 'teacher_form.html', context)
