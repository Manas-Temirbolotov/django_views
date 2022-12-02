from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Student, Course
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'course_list.html', context)

def course_create(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('course_list'))
    context = {
        'form': form
    }
    return render(request, 'course_form.html', context)



