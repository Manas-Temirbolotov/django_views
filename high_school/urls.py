from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('teacher_create/', views.teacher_create, name='teacher_create'),
    path('teacher/<int:id>/', views.teacher_detail, name='teacher_detail'),
    path('teacher/<int:id>/update/', views.teacher_update, name='teacher_update'),
    path('teacher/<int:id>/delete/', views.teacher_delete, name='teacher_delete'),

#     Школьники

    path('pupil/list/', views.PupilListView.as_view(), name='pupil_list'),
    path('pupil/create/', views.PupilListView.as_view(), name='pupil_create'),
    path('pupil/<int:pk>/', views.PupilDetailView.as_view(), name='pupil_detail'),
    path('pupil/<int:pk>/update', views.PupilUpdateView.as_view(), name='pupil_update'),
    path('pupil/<int:pk>/delete', views.PupilDeleteView.as_view(), name='pupil_delete'),

]