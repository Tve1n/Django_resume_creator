from django.urls import path
from resume import views

urlpatterns = [
    path('', views.resume_form, name='resume_form'),
    path('success/', views.resume_success, name='resume_success'),
    path('view/', views.resume_view, name='resume_view'),
    path('list/', views.resume_list, name='resume_list'),
    path('resume/<int:pk>/', views.resume_detail, name='resume_detail'),
]