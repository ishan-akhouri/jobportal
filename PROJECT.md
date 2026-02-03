# Job Portal Project

## Overview
A Django-based job portal connecting job seekers with employers.

**Tech Stack:**
- Python 3.13
- Django 6.0
- SQLite (development)
- Running on: Mac (local development)

---

## Current Status: Phase 1 Complete ✅

### Completed Features
- ✅ Django project structure
- ✅ Custom User model (job_seeker/employer types)
- ✅ Job model (posting details)
- ✅ Application model (job applications)
- ✅ JobSeekerProfile & EmployerProfile models
- ✅ Admin interface configured
- ✅ Database migrations working

### Database Schema
**Users Table:**
- Custom User extending AbstractUser
- Fields: username, email, password, user_type, phone

**Jobs Table:**
- title, description, requirements, location
- job_type, salary_min, salary_max
- employer (FK to User), is_active, timestamps

**Applications Table:**
- job (FK), applicant (FK), cover_letter, status
- Unique constraint: one application per job per user

**Profiles:**
- JobSeekerProfile: resume, skills, experience_years, education
- EmployerProfile: company_name, company_description, website

---

## Phase 2: Authentication & User Management (IN PROGRESS)

### Goals
- User registration (separate flows for job seekers & employers)
- Login/logout system
- Profile pages (view & edit)
- Role-based dashboards

### Tasks
- [ ] URL structure setup
- [ ] Templates folder & base template
- [ ] Registration views & forms
- [ ] Login/logout views
- [ ] Profile display pages
- [ ] Profile edit forms
- [ ] Dashboards (job seeker & employer)

---

## Phase 3: Job Management (PLANNED)

### For Employers
- Post new jobs
- View/edit/delete their jobs
- View applications received

### For Job Seekers
- Browse all active jobs
- Search & filter jobs
- View job details
- Save jobs (optional)

---

## Phase 4: Application System (PLANNED)

- Job seekers apply to jobs
- Resume upload
- Employers review applications
- Status management (pending/reviewed/interview/rejected/accepted)
- Application tracking

---

## Phase 5: Polish & Enhancements (PLANNED)

- Email notifications
- Advanced search & filters
- Analytics for employers
- Better UI/UX styling
- Company profiles

---

## Development Workflow
```bash
# Activate virtual environment
source venv/bin/activate

# Run migrations (if models changed)
python manage.py makemigrations
python manage.py migrate

# Run development server
python manage.py runserver

# Access admin: http://127.0.0.1:8000/admin
```

## Project Structure
```
jobportal/
├── manage.py
├── config/          # Project settings
├── users/           # User management app
├── jobs/            # Jobs and applications app
├── companies/       # Company profiles (future)
├── templates/       # HTML templates (to be created)
├── static/          # CSS, JS, images (to be created)
└── media/           # User uploads (resumes, etc.)
```

---

## Notes
- Solo project for learning Django
- Mac-only development
- SQLite for simplicity
- Focus on functionality first, polish later
