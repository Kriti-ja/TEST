# labour_dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.labour_dashboard, name='labour_dashboard'),
]
