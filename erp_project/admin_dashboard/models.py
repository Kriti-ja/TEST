from django.db import models
from user_management.models import User

class Labour(models.Model):
    AREA_CHOICES = [
        ('Noida', 'Noida'),
        ('Delhi', 'Delhi'),
        ('Greater Noida', 'Greater Noida'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sales_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_labours')
    area = models.CharField(max_length=20, choices=AREA_CHOICES)
    in_time = models.DateTimeField(null=True, blank=True)
    out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.area}"

class LocationTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # For Sales Managers and Labours only
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # Latitude coordinate
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Longitude coordinate
    timestamp = models.DateTimeField(auto_now_add=True)  # When the location was recorded

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"