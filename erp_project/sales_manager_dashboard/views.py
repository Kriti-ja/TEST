from django.shortcuts import render, get_object_or_404,redirect
from admin_dashboard.models import Labour
from labour_dashboard.models import Task
from user_management.models import User
from django.utils import timezone
from django.http import HttpResponse
from django.http import HttpResponseForbidden
def labour_task_status(request, labour_id):
    labour = get_object_or_404(Labour, id=labour_id, sales_manager=request.user)
    tasks = Task.objects.filter(labour=labour).order_by('deadline')  # Tasks ordered by deadline for easier tracking

    # Check if tasks are overdue
    for task in tasks:
        if task.status == 'pending' and task.deadline < timezone.now().date():
            task.status = 'overdue'
            task.save()

    return render(request, 'sales_manager_dashboard/labour_task_status.html', {
        'labour': labour,
        'tasks': tasks,
    })
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from admin_dashboard.models import Labour

@login_required
def sales_manager_dashboard(request):
    if request.user.role != 'sales_manager':
        return HttpResponseForbidden("Access Denied")
    labours = Labour.objects.filter(sales_manager=request.user)
    return render(request, 'sales_manager_dashboard/sales_manager_dashboard.html', {
        'labours': labours,
    })

@login_required
def create_task(request, labour_id):
    labour = get_object_or_404(Labour, id=labour_id)
    
    if request.method == 'POST':
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        
        Task.objects.create(
            labour=labour,
            description=description,
            deadline=deadline
        )
        
        return redirect('sales_manager_dashboard')
    
    return render(request, 'sales_manager_dashboard/create_task.html', {'labour': labour})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.description = request.POST.get('description')
        task.deadline = request.POST.get('deadline')
        task.save()
        
        return redirect('sales_manager_dashboard')
    
    return render(request, 'sales_manager_dashboard/edit_task.html', {'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('sales_manager_dashboard')
    return render(request, 'sales_manager_dashboard/confirm_delete_task.html', {'task': task})

def home(request):
    return HttpResponse("Welcome to the ERP System!")
