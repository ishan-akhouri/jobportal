from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, JobSeekerProfile, EmployerProfile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'user_type', 'first_name', 'last_name']
    list_filter = ['user_type', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('user_type', 'phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('user_type', 'phone')}),
    )

@admin.register(JobSeekerProfile)
class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'experience_years', 'education']
    search_fields = ['user__username', 'skills']

@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'website']
    search_fields = ['company_name', 'user__username']
