from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


class Task(models.Model):
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.CharField(choices=[
        ('No', 'Incomplete'),
        ('Yes', 'Complete')], default='No')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return f"{self.title} | {self.assignee}"

    def is_overdue(self):
        return self.due_date < timezone.now().date() and self.is_completed == 'No'