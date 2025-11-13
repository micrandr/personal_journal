from django.shortcuts import render, redirect
from .models import JournalEntry

def home(request):
    entries = JournalEntry.objects.all().order_by('-created_at')
    return render(request, 'journal/home.html', {'entries': entries})
