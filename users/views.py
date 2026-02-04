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
