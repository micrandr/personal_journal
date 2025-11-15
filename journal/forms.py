from django import forms
from .models import JournalEntry

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300',
                'placeholder': 'Enter title...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-3 border rounded-lg h-40 focus:outline-none focus:ring focus:ring-blue-300',
                'placeholder': 'Write journal content...'
            }),
        }
