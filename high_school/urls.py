from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('teacher_create/', views.teacher_create, name='teacher_create'),

]