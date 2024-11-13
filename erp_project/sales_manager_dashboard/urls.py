# sales_manager_dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('labour/<int:labour_id>/tasks/', views.labour_task_status, name='labour_task_status'),
]
