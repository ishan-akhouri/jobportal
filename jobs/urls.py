# jobs/urls.py
from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    # Job browsing (for job seekers)
    path('', views.job_list_view, name='job_list'),
    path('<int:pk>/', views.job_detail_view, name='job_detail'),
    path('<int:pk>/apply/', views.apply_to_job, name='apply'),
    path('my-applications/', views.my_applications_view, name='my_applications'),
    
    # Job posting (for employers)
    path('post/', views.post_job_view, name='post_job'),
    path('my-jobs/', views.my_jobs_view, name='my_jobs'),
    path('<int:pk>/edit/', views.edit_job_view, name='edit_job'),
    path('<int:pk>/delete/', views.delete_job_view, name='delete_job'),
    path('<int:pk>/applications/', views.job_applications_view, name='job_applications'),
]