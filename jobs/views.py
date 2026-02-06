# jobs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Job, Application
from .forms import JobSearchForm


def job_list_view(request):
    """
    Display list of all active jobs with search and filter functionality.
    Available to all users (authenticated or not).
    """
    # Get all active jobs
    jobs = Job.objects.filter(is_active=True)
    
    # Initialize search form
    form = JobSearchForm(request.GET or None)
    
    # Apply filters if form is valid
    if form.is_valid():
        search_query = form.cleaned_data.get('search')
        location = form.cleaned_data.get('location')
        job_type = form.cleaned_data.get('job_type')
        
        # Search by title or description
        if search_query:
            jobs = jobs.filter(
                Q(title__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        # Filter by location
        if location:
            jobs = jobs.filter(location__icontains=location)
        
        # Filter by job type
        if job_type:
            jobs = jobs.filter(job_type=job_type)
    
    # Order by most recent first
    jobs = jobs.order_by('-created_at')
    
    context = {
        'jobs': jobs,
        'form': form,
        'total_jobs': jobs.count(),
    }
    
    return render(request, 'jobs/job_list.html', context)


def job_detail_view(request, pk):
    """
    Display detailed information about a specific job.
    Shows apply button for job seekers.
    """
    job = get_object_or_404(Job, pk=pk, is_active=True)
    
    # Check if user has already applied (if authenticated and job seeker)
    has_applied = False
    if request.user.is_authenticated and request.user.user_type == 'job_seeker':
        has_applied = Application.objects.filter(
            job=job,
            applicant=request.user
        ).exists()
    
    context = {
        'job': job,
        'has_applied': has_applied,
    }
    
    return render(request, 'jobs/job_detail.html', context)