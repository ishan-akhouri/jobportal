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
]