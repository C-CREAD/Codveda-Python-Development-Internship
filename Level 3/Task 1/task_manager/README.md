# Django: Task Manager Web Application with Authentication

## Description: Task 1 - Django Web Application with Authentication

Build a fully functional web application using Django that includes user authentication (login, registration, and password reset). The application can be a blog, task manager, or e-commerce site

## Objectives
✅ - Implement user registration, login, and logout functionality.

✅ - Secure user passwords using Django’s built-in authentication system.

✅ - Create user roles (e.g., admin, regular user) with different permissions.

✅ - Integrate password reset functionality via email. (To ensure this feature works, all admin/non-admin users must be registered with a valid email address.)

NOTE: Some features of the project are admin-only, thus, logging in as a non-admin user will show fewer features.

## Installation
1. Navigate to the terminal, then go to the 'task_manager' directory where manage.py resides.
   ```sh
   cd task_manager
   ```

2. Run the following commands in order:
   ```sh
   pip install -r requirements.txt
   ```
   ```sh
   python makemigrations tasks
   ```
   ```sh
   python manage.py migrate
   ```
   ```sh
   python manage.py createsuperuser
   ```
   Enter your own admin credentials
   
   ```sh
   python manage.py runserver
   ```

3. Create your .env file according to this example format. (Required for accessing Password Reset Feature)
   ```sh
   EMAIL_HOST_USER='your-host-email@gmail.com'
   EMAIL_HOST_PASSWORD='your-app-password'
   SECRET_KEY='your-secret-key'
   ```

6. Go to the browser and access the following link: http://127.0.0.1:8000/

## Credit
Created By: [Shingai Dzinotyiweyi](https://github.com/C-CREAD)
