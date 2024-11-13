from django.db import models
from admin_dashboard.models import Labour
from django.utils import timezone

class Task(models.Model):
    labour = models.ForeignKey(Labour, on_delete=models.CASCADE, related_name="tasks")
    description = models.TextField()  # Description of the task
    date_assigned = models.DateField(auto_now_add=True)
    deadline = models.DateField()  # Deadline for task completion
    completion_date = models.DateField(null=True, blank=True)  # Date when task was completed
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def mark_completed(self):
        """Mark the task as completed and set the completion date."""
        self.status = 'completed'
        self.completion_date = timezone.now()
        self.save()

    def __str__(self):
        return f"Task for {self.labour.user.username} - {self.description[:20]} (Status: {self.status})"
