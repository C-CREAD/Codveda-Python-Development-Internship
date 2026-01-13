from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('add-task/', views.add_task, name='add_task'),
    path('view-all-tasks/', views.view_all_tasks, name='view_all_tasks'),
    path('view-my-tasks/', views.view_my_tasks, name='view_my_tasks'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('mark-complete/<int:task_id>/', views.mark_complete, name='mark_complete'),
    path('reports/', views.generate_reports, name='reports'),
]