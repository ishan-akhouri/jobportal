#/users/urls.py
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/job-seeker/', views.register_job_seeker, name='register_job_seeker'),
    path('register/employer/', views.register_employer, name='register_employer'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
]