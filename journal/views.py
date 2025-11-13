from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import JournalEntryForm
from .models import JournalEntry



def home(request):
    entries = JournalEntry.objects.all().order_by('-created_at')
    return render(request, 'journal/home.html', {'entries': entries})

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