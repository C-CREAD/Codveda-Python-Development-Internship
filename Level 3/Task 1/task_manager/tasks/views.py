from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task
from .forms import UserForm, TaskForm, EditTaskForm
from datetime import datetime


def login_user(request):
    """
    Checks if the user is logged in,
    else, redirect them back to the login page.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html',
                          {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def logout_user(request):
    """
    Logs the user out of the session, then redirect them back to the login page.
    """
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    """
    Renders the home page and displays relevant logged-in user information 
    """
    user = request.user
    user_task_count = Task.objects.filter(assignee=user).count()
    user_incomplete = Task.objects.filter(assignee=user, is_completed='No').count()
    user_complete = Task.objects.filter(assignee=user, is_completed='Yes').count()
    context = {
        'current_date': datetime.today().date(),
        'is_admin': user.is_staff,
        'user_task_count': user_task_count,
        'user_incomplete': user_incomplete,
        'user_complete': user_complete,
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def register_user(request):
    """
    Renders the 'register user' page and saves new users to the database
    """
    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()

    return render(request, 'registration.html', {'form': form})


@login_required(login_url='login')
def add_task(request):
    """
    Renders the 'add task' page and saves new tasks to the database
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_all_tasks')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})


@login_required(login_url='login')
def view_all_tasks(request):
    """
    Renders the 'View all tasks' page and displays all task information. (Only accessible by admin users) 
    """
    if not request.user.is_staff:
        return redirect('home')

    tasks = Task.objects.all().order_by('due_date')
    context = {'tasks': tasks}
    return render(request, 'view_all_tasks.html', context)


@login_required(login_url='login')
def view_my_tasks(request):
    """
    Renders the 'View my tasks' page and displays all task information assigned to the logged-in user.
    """
    user = request.user
    tasks = Task.objects.filter(assignee=user).order_by('due_date')
    context = {'tasks': tasks}
    return render(request, 'view_my_tasks.html', context)


@login_required(login_url='login')
def edit_task(request, task_id):
    """
    Renders the 'edit task' page and saves the new changes of the selected task to the database
    """
    task = get_object_or_404(Task, id=task_id)

    if task.assignee != request.user:
        return redirect('view_my_tasks')

    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_my_tasks')
    else:
        form = EditTaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})


@login_required(login_url='login')
def mark_complete(request, task_id):
    """
    Marks the selected task as complete, then redirects back to the 'view my tasks' page.
    """
    task = get_object_or_404(Task, id=task_id)

    if task.assignee != request.user:
        return redirect('view_my_tasks')

    if task.is_completed == 'No':
        task.is_completed = 'Yes'
        task.save()

    return redirect('view_my_tasks')


@login_required(login_url='login')
def generate_reports(request):
    """
    Generates statistics based on the total No. of users & tasks.
    Other stats include:
    - Total assigned tasks and per user
    - Complete/Incomplete/Overdue tasks
    - Percentages based on assigned tasks

    """
    if not request.user.is_staff:
        return redirect('home')

    users = User.objects.all()
    user_stats = {}

    total_tasks = Task.objects.count()

    for user in users:
        user_tasks = Task.objects.filter(assignee=user)
        assigned_count = user_tasks.count()
        completed_count = user_tasks.filter(is_completed='Yes').count()
        incomplete_count = user_tasks.filter(is_completed='No').count()
        overdue_count = user_tasks.filter(
            is_completed='No',
            due_date__lt=timezone.now().date()
        ).count()

        if total_tasks > 0:
            assigned_percentage = round((assigned_count / total_tasks) * 100, 2)
            completed_percentage = round((completed_count / total_tasks) * 100, 2)
            incomplete_percentage = round((incomplete_count / total_tasks) * 100, 2)
            overdue_percentage = round((overdue_count / total_tasks) * 100, 2)
        else:
            assigned_percentage = completed_percentage = incomplete_percentage = overdue_percentage = 0

        user_stats[user.username] = {
            'assigned': assigned_count,
            'assigned_percentage': assigned_percentage,
            'completed_percentage': completed_percentage,
            'incomplete_percentage': incomplete_percentage,
            'overdue_percentage': overdue_percentage,
        }

    completed_tasks = Task.objects.filter(is_completed='Yes').count()
    incomplete_tasks = Task.objects.filter(is_completed='No').count()
    overdue_tasks = Task.objects.filter(
        is_completed='No',
        due_date__lt=timezone.now().date()
    ).count()

    if total_tasks > 0:
        incomplete_percentage = round((incomplete_tasks / total_tasks) * 100, 2)
        overdue_percentage = round((overdue_tasks / total_tasks) * 100, 2)
    else:
        incomplete_percentage = overdue_percentage = 0

    task_stats = {
        'total': total_tasks,
        'completed': completed_tasks,
        'incomplete': incomplete_tasks,
        'overdue': overdue_tasks,
        'incomplete_percentage': incomplete_percentage,
        'overdue_percentage': overdue_percentage,
    }

    context = {
        'user_stats': user_stats,
        'task_stats': task_stats,
    }

    return render(request, 'reports.html', context)
