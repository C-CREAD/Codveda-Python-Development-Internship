from django.contrib import admin

# Register your models here.
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'assignee', 'due_date', 'is_completed', 'is_overdue']
    list_filter = ['is_completed', 'due_date', 'created_at']
    search_fields = ['title', 'description', 'assignee__username']
    ordering = ['due_date']