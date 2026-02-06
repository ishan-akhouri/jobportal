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


class JobPostForm(forms.ModelForm):
    """
    Form for employers to create and edit job postings.
    """
    class Meta:
        model = Job
        fields = ['title', 'description', 'requirements', 'location', 'job_type', 'salary_min', 'salary_max']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Senior Python Developer'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the role, responsibilities, and what makes this opportunity great...',
                'rows': 6
            }),
            'requirements': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'List required skills, qualifications, and experience...',
                'rows': 6
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., San Francisco, CA or Remote'
            }),
            'job_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'salary_min': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Minimum salary (optional)',
                'min': 0
            }),
            'salary_max': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Maximum salary (optional)',
                'min': 0
            }),
        }
        labels = {
            'title': 'Job Title',
            'description': 'Job Description',
            'requirements': 'Requirements & Qualifications',
            'location': 'Location',
            'job_type': 'Job Type',
            'salary_min': 'Minimum Salary (Optional)',
            'salary_max': 'Maximum Salary (Optional)',
        }
    
    def __init__(self, *args, **kwargs):
        self.employer = kwargs.pop('employer', None)
        super().__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        salary_min = cleaned_data.get('salary_min')
        salary_max = cleaned_data.get('salary_max')
        
        # Validate salary range
        if salary_min and salary_max:
            if salary_min > salary_max:
                raise forms.ValidationError('Minimum salary cannot be greater than maximum salary.')
        
        return cleaned_data
    
    def save(self, commit=True):
        job = super().save(commit=False)
        job.employer = self.employer
        job.is_active = True
        
        if commit:
            job.save()
        
        return job