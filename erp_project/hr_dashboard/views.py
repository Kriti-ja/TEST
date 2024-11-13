from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from hr_dashboard.models import Attendance, Salary
from user_management.models import User
from django.http import HttpResponseForbidden
@login_required
def hr_dashboard(request):
    if request.user.role != 'hr':
        return HttpResponseForbidden("Access Denied")
    employees = User.objects.all()
    return render(request, 'hr_dashboard/hr_dashboard.html', {
        'employees': employees,
    })

@login_required
def manage_attendance(request):
    if request.user.role != 'hr':
        return HttpResponseForbidden("Access Denied")
    attendance_records = Attendance.objects.all()
    return render(request, 'hr_dashboard/manage_attendance.html', {
        'attendance_records': attendance_records,
    })

@login_required
def manage_salaries(request):
    if request.user.role != 'hr':
        return HttpResponseForbidden("Access Denied")
    salaries = Salary.objects.all()
    return render(request, 'hr_dashboard/manage_salaries.html', {
        'salaries': salaries,
    })
