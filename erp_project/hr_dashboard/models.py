# hr_dashboard/models.py
from django.db import models
from admin_dashboard.models import Labour
from user_management.models import User


class Attendance(models.Model):
    labour = models.ForeignKey(Labour, on_delete=models.CASCADE, related_name="attendance_records")
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

    def __str__(self):
        return f"{self.labour.user.username} - {self.date} - {self.status}"

class Salary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="salaries")
    month = models.CharField(max_length=20)  # E.g., "January 2024"
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class PayrollAdjustment(models.Model):
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE, related_name="adjustments")
    adjustment_type = models.CharField(max_length=50)  # E.g., 'Bonus', 'Deduction'
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.adjustment_type} for {self.salary.user.username} - {self.amount}"