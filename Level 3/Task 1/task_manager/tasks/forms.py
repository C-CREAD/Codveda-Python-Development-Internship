from django import forms
from .models import Task
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    """
    Class Form for creating User objects
    """
    email = forms.EmailField(label='Email Address',widget=forms.EmailInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken!")
        if username and len(username.strip()) == 0:
            raise forms.ValidationError("Username cannot be empty!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered!")
        if email and len(email.strip()) == 0:
            raise forms.ValidationError("Email cannot be empty!")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 1:
            raise forms.ValidationError("Password cannot be empty.")
        return password

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')

        # Verify passwords
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        return clean_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class TaskForm(forms.ModelForm):
    """
    Class Form for creating and updating Task objects
    """
    assignee = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Assign a task to a user'
    )

    class Meta:
        model = Task
        fields = ['assignee', 'title', 'description', 'due_date', 'is_completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter task title'}),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date:
            from datetime import date
            if due_date < date.today():
                raise forms.ValidationError("Due date cannot be in the past!")
        return due_date

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and len(title.strip()) == 0:
            raise forms.ValidationError("Title cannot be empty!")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description.strip()) == 0:
            raise forms.ValidationError("Description cannot be empty!")
        return description


class EditTaskForm(forms.ModelForm):
    """
    Class Form for updating Task objects
    """
    assignee = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label="Reassign task (leave empty to skip)"
    )

    class Meta:
        model = Task
        fields = ['assignee', 'due_date', 'is_completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }