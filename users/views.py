#/users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import JobSeekerRegistrationForm, EmployerRegistrationForm

def home(request):
    """
    Home page view - landing page for the job portal.
    """
    return render(request, 'home.html')


def register_job_seeker(request):
    """
    Registration view for job seekers.
    """
    if request.user.is_authenticated:
        # Already logged in, redirect to home
        return redirect('home')
    
    if request.method == 'POST':
        form = JobSeekerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}! You can now log in.')
            return redirect('users:login')
    else:
        form = JobSeekerRegistrationForm()
    
    return render(request, 'users/register_job_seeker.html', {'form': form})


def register_employer(request):
    """
    Registration view for employers.
    """
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Employer account created for {user.username}! You can now log in.')
            return redirect('users:login')
    else:
        form = EmployerRegistrationForm()
    
    return render(request, 'users/register_employer.html', {'form': form})

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    """
    Login view for all users (job seekers and employers).
    After login, redirects to appropriate dashboard.
    """
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                # Redirect based on user type
                return redirect('home')  # For now, just go home. Later we'll add dashboards.
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    """
    Logout view - logs out user and redirects to home.
    """
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def profile_view(request):
    """
    Display user profile (read-only).
    Shows different information based on user type.
    """
    user = request.user
    
    if user.user_type == 'job_seeker':
        try:
            profile = user.jobseekerprofile
        except:
            # Create profile if it doesn't exist
            from .models import JobSeekerProfile
            profile = JobSeekerProfile.objects.create(user=user)
        
        return render(request, 'users/profile.html', {
            'profile': profile,
            'user_type': 'job_seeker'
        })
    else:  # employer
        try:
            profile = user.employerprofile
        except:
            # Create profile if it doesn't exist
            from .models import EmployerProfile
            profile = EmployerProfile.objects.create(user=user, company_name='Not Set')
        
        return render(request, 'users/profile.html', {
            'profile': profile,
            'user_type': 'employer'
        })


@login_required
def profile_edit_view(request):
    """
    Edit user profile.
    Uses different forms based on user type.
    """
    user = request.user
    
    if user.user_type == 'job_seeker':
        try:
            profile = user.jobseekerprofile
        except:
            from .models import JobSeekerProfile
            profile = JobSeekerProfile.objects.create(user=user)
        
        if request.method == 'POST':
            from .forms import JobSeekerProfileEditForm
            form = JobSeekerProfileEditForm(request.POST, request.FILES, instance=profile, user=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated successfully!')
                return redirect('users:profile')
        else:
            from .forms import JobSeekerProfileEditForm
            form = JobSeekerProfileEditForm(instance=profile, user=user)
        
        return render(request, 'users/profile_edit.html', {
            'form': form,
            'user_type': 'job_seeker'
        })
    
    else:  # employer
        try:
            profile = user.employerprofile
        except:
            from .models import EmployerProfile
            profile = EmployerProfile.objects.create(user=user, company_name='Not Set')
        
        if request.method == 'POST':
            from .forms import EmployerProfileEditForm
            form = EmployerProfileEditForm(request.POST, instance=profile, user=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated successfully!')
                return redirect('users:profile')
        else:
            from .forms import EmployerProfileEditForm
            form = EmployerProfileEditForm(instance=profile, user=user)
        
        return render(request, 'users/profile_edit.html', {
            'form': form,
            'user_type': 'employer'
        })