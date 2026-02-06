# jobs/forms.py
from django import forms
from .models import Job

class JobSearchForm(forms.Form):
    """
    Form for searching and filtering jobs.
    """
    search = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by job title or keywords...'
        })
    )
    
    location = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Location (optional)'
        })
    )
    
    job_type = forms.ChoiceField(
        required=False,
        choices=[('', 'All Job Types')] + list(Job.JOB_TYPES),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )