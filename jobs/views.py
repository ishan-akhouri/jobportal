# jobs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Job, Application
from .forms import JobSearchForm, JobApplicationForm, JobPostForm


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


@login_required
def apply_to_job(request, pk):
    """
    Job application view - job seekers apply to a job with cover letter.
    Only accessible to job seekers.
    """
    # Check if user is a job seeker
    if request.user.user_type != 'job_seeker':
        messages.error(request, 'Only job seekers can apply to jobs.')
        return redirect('jobs:job_detail', pk=pk)
    
    # Get the job
    job = get_object_or_404(Job, pk=pk, is_active=True)
    
    # Check if already applied
    existing_application = Application.objects.filter(
        job=job,
        applicant=request.user
    ).first()
    
    if existing_application:
        messages.warning(request, 'You have already applied to this job.')
        return redirect('jobs:job_detail', pk=pk)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, job=job, applicant=request.user)
        if form.is_valid():
            application = form.save()
            messages.success(request, f'Your application to {job.title} has been submitted successfully!')
            return redirect('jobs:my_applications')
    else:
        form = JobApplicationForm(job=job, applicant=request.user)
    
    context = {
        'form': form,
        'job': job,
    }
    
    return render(request, 'jobs/apply.html', context)


@login_required
def my_applications_view(request):
    """
    Display all applications submitted by the logged-in job seeker.
    Only accessible to job seekers.
    """
    # Check if user is a job seeker
    if request.user.user_type != 'job_seeker':
        messages.error(request, 'Only job seekers can view applications.')
        return redirect('users:dashboard')
    
    # Get all applications by this user
    applications = Application.objects.filter(
        applicant=request.user
    ).select_related('job', 'job__employer').order_by('-applied_at')
    
    context = {
        'applications': applications,
    }
    
    return render(request, 'jobs/my_applications.html', context)


@login_required
def post_job_view(request):
    """
    Job posting view - employers create new job listings.
    Only accessible to employers.
    """
    # Check if user is an employer
    if request.user.user_type != 'employer':
        messages.error(request, 'Only employers can post jobs.')
        return redirect('users:dashboard')
    
    if request.method == 'POST':
        form = JobPostForm(request.POST, employer=request.user)
        if form.is_valid():
            job = form.save()
            messages.success(request, f'Job "{job.title}" has been posted successfully!')
            return redirect('jobs:my_jobs')
    else:
        form = JobPostForm(employer=request.user)
    
    context = {
        'form': form,
    }
    
    return render(request, 'jobs/post_job.html', context)


@login_required
def my_jobs_view(request):
    """
    Display all jobs posted by the logged-in employer.
    Only accessible to employers.
    """
    # Check if user is an employer
    if request.user.user_type != 'employer':
        messages.error(request, 'Only employers can view posted jobs.')
        return redirect('users:dashboard')
    
    # Get all jobs posted by this employer
    jobs = Job.objects.filter(employer=request.user).order_by('-created_at')
    
    # Get application counts for each job
    for job in jobs:
        job.application_count = Application.objects.filter(job=job).count()
    
    context = {
        'jobs': jobs,
    }
    
    return render(request, 'jobs/my_jobs.html', context)


@login_required
def edit_job_view(request, pk):
    """
    Edit an existing job posting.
    Only accessible to the employer who created the job.
    """
    # Get the job
    job = get_object_or_404(Job, pk=pk)
    
    # Check if user is an employer
    if request.user.user_type != 'employer':
        messages.error(request, 'Only employers can edit jobs.')
        return redirect('jobs:job_detail', pk=pk)
    
    # Check if user owns this job
    if job.employer != request.user:
        messages.error(request, 'You can only edit your own job postings.')
        return redirect('jobs:job_detail', pk=pk)
    
    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=job, employer=request.user)
        if form.is_valid():
            job = form.save()
            messages.success(request, f'Job "{job.title}" has been updated successfully!')
            return redirect('jobs:my_jobs')
    else:
        form = JobPostForm(instance=job, employer=request.user)
    
    context = {
        'form': form,
        'job': job,
        'editing': True,
    }
    
    return render(request, 'jobs/edit_job.html', context)


@login_required
def delete_job_view(request, pk):
    """
    Delete a job posting.
    Only accessible to the employer who created the job.
    """
    # Get the job
    job = get_object_or_404(Job, pk=pk)
    
    # Check if user is an employer
    if request.user.user_type != 'employer':
        messages.error(request, 'Only employers can delete jobs.')
        return redirect('jobs:job_detail', pk=pk)
    
    # Check if user owns this job
    if job.employer != request.user:
        messages.error(request, 'You can only delete your own job postings.')
        return redirect('jobs:job_detail', pk=pk)
    
    if request.method == 'POST':
        job_title = job.title
        job.delete()
        messages.success(request, f'Job "{job_title}" has been deleted successfully!')
        return redirect('jobs:my_jobs')
    
    context = {
        'job': job,
    }
    
    return render(request, 'jobs/delete_job.html', context)


@login_required
def job_applications_view(request, pk):
    """
    View all applications for a specific job.
    Only accessible to the employer who posted the job.
    """
    # Get the job
    job = get_object_or_404(Job, pk=pk)
    
    # Check if user is an employer
    if request.user.user_type != 'employer':
        messages.error(request, 'Only employers can view applications.')
        return redirect('jobs:job_detail', pk=pk)
    
    # Check if user owns this job
    if job.employer != request.user:
        messages.error(request, 'You can only view applications for your own job postings.')
        return redirect('jobs:job_detail', pk=pk)
    
    # Get all applications for this job
    applications = Application.objects.filter(job=job).select_related(
        'applicant', 'applicant__jobseekerprofile'
    ).order_by('-applied_at')
    
    context = {
        'job': job,
        'applications': applications,
    }
    
    return render(request, 'jobs/job_applications.html', context)