from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from user_management.models import User
from admin_dashboard.models import Labour, LocationTracking
from django.http import HttpResponseForbidden 
@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return HttpResponseForbidden("Access Denied")
    sales_managers = User.objects.filter(role='sales_manager')
    labours = Labour.objects.all()
    return render(request, 'admin_dashboard/admin_dashboard.html', {
        'sales_managers': sales_managers,
        'labours': labours,
    })

@login_required
def view_locations(request):
    if request.user.role != 'admin':
        return HttpResponseForbidden("Access Denied")
    locations = LocationTracking.objects.all()  # Admin can view all location data
    return render(request, 'admin_dashboard/view_locations.html', {
        'locations': locations,
    })

@login_required
def manage_labours(request):
    if request.user.role != 'admin':
        return HttpResponseForbidden("Access Denied")
    labours = Labour.objects.all()
    return render(request, 'admin_dashboard/manage_labours.html', {
        'labours': labours,
    })

@login_required
def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        
        user = User.objects.create(username=username, email=email)
        user.role = role
        user.save()
        
        return redirect('admin_dashboard')
    return render(request, 'admin_dashboard/create_user.html')



@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.role = request.POST.get('role')
        user.save()
        
        return redirect('admin_dashboard')
    
    return render(request, 'admin_dashboard/edit_user.html', {'user': user})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('admin_dashboard')
    return render(request, 'admin_dashboard/confirm_delete.html', {'user': user})
