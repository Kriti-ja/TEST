from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('view-locations/', views.view_locations, name='view_locations'),
    path('manage-labours/', views.manage_labours, name='manage_labours'),
]
