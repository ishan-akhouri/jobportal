# jobs/forms.py
from django import forms
from .models import Job, Application

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


class JobApplicationForm(forms.ModelForm):
    """
    Form for job seekers to apply to a job.
    Includes cover letter field.
    """
    class Meta:
        model = Application
        fields = ['cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a cover letter explaining why you\'re a great fit for this position...',
                'rows': 8
            })
        }
        labels = {
            'cover_letter': 'Cover Letter (Optional)'
        }
    
    def __init__(self, *args, **kwargs):
        self.job = kwargs.pop('job', None)
        self.applicant = kwargs.pop('applicant', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        application = super().save(commit=False)
        application.job = self.job
        application.applicant = self.applicant
        application.status = 'pending'
        
        if commit:
            application.save()
        
        return application