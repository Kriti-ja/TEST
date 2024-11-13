# hr_dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hr_dashboard, name='hr_dashboard'),
    path('manage-attendance/', views.manage_attendance, name='manage_attendance'),
    path('manage-salaries/', views.manage_salaries, name='manage_salaries'),
]
