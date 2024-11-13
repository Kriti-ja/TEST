from django.db import models
from user_management.models import User
from admin_dashboard.models import Labour

class LabourAssignment(models.Model):
    sales_manager = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'sales_manager'})
    labour = models.ForeignKey(Labour, on_delete=models.CASCADE)
    assigned_area = models.CharField(max_length=50, choices=[('Noida', 'Noida'), ('Delhi', 'Delhi'), ('Greater Noida', 'Greater Noida')])
    assignment_date = models.DateField(auto_now_add=True)  # Date the assignment was made

    def __str__(self):
        return f"{self.sales_manager.username} manages {self.labour.user.username} in {self.assigned_area}"
