from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('course/<int:id>/update/', views.course_update, name='course_update'),
    path('course/<int:id>/delete/', views.course_delete, name='course_delete'),
    #     Студенты
    path('student/list/', views.StudentListView.as_view(), name='student_list'),
    path('student/create/', views.StudentListView.as_view(), name='student_create'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/<int:pk>/update', views.StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete', views.StudentDeleteView.as_view(), name='student_delete'),


]