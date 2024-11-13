from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from labour_dashboard.models import Task

@login_required
def labour_dashboard(request):
    if request.user.role != 'labour':
        return HttpResponseForbidden("Access Denied")
    tasks = Task.objects.filter(labour__user=request.user)
    return render(request, 'labour_dashboard/labour_dashboard.html', {
        'tasks': tasks,
    })
