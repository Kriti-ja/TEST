from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('sales_manager', 'Sales Manager'),
        ('labour', 'Labour'),
        ('hr', 'HR Department'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    admin_id = models.CharField(max_length=10, null=True, blank=True)  # Predefined for Admins only

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
