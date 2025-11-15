from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import JournalEntryForm
from .models import JournalEntry



def home(request):
    entries = JournalEntry.objects.all().order_by('-created_at')
    return render(request, 'journal/home.html', {'entries': entries})

"""
Login Component
---------------

This component handles user authentication for the application.

Features:
- Displays a login form for registered users.
- Validates submitted credentials using Django's built-in auth system.
- Redirects authenticated users to the dashboard or a specified next page.

Usage:
- Included in the accounts app as the login view.
- Connected to the URL: /accounts/login/
- Works together with Django's LoginView or a custom login form.

Notes:
- Make sure 'django.contrib.auth' is enabled in INSTALLED_APPS.
- CSRF protection is enabled by default.
- Customize templates in templates/accounts/login.html as needed.
"""
@login_required
def add_entry(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JournalEntryForm()
    return render(request, 'journal/add_entry.html', {'form': form})

"""
Signup Component
----------------

This module manages user registration for the application.

Features:
- Provides a registration form for new users.
- Validates required fields (username, email, password).
- Uses Django's built-in User model or a custom user model.
- Hashes and securely stores user passwords.
- Automatically logs in the user after successful registration (optional).
- Redirects newly registered users to their dashboard or a welcome page.

Usage:
- Part of the accounts app under /accounts/signup/
- Connected to a Django Form or ModelForm for input validation.
- Template located in personal_journal/templates/registration/signup.html

Notes:
- Ensure password validation settings are configured in settings.py.
- Consider adding email verification depending on the project's needs.
"""

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatically log the user in
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})