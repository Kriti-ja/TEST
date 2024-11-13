# hr_dashboard/admin.py
from django.contrib import admin
from .models import Attendance, Salary, PayrollAdjustment

admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(PayrollAdjustment)
