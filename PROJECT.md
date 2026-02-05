# Job Portal Project

## Overview
A Django-based job portal connecting job seekers with employers.

Tech Stack:
- Python 3.13
- Django 6.0
- SQLite (development)
- Bootstrap 5 (CDN)
- Running on: Mac (local development)

---

## Current Status: Phase 2 - 60% Complete

### Phase 1: Complete
- Django project structure
- Custom User model (job_seeker/employer types)
- Job model (posting details)
- Application model (job applications)
- JobSeekerProfile & EmployerProfile models
- Admin interface configured
- Database migrations working

### Phase 2: Authentication & User Management (IN PROGRESS)
- DONE Task 1: URL structure & templates setup
- DONE Task 2: Registration system (job seekers & employers)
- DONE Task 3: Login/logout functionality
- TODO Task 4: Profile pages (view & edit)
- TODO Task 5: Role-based dashboards

---

## Database Schema

Users Table:
- Custom User extending AbstractUser
- Fields: username, email, password, user_type, phone, first_name, last_name

Jobs Table:
- title, description, requirements, location
- job_type, salary_min, salary_max
- employer (FK to User), is_active, timestamps

Applications Table:
- job (FK), applicant (FK), cover_letter, status
- Unique constraint: one application per job per user

Profiles:
- JobSeekerProfile: resume, skills, experience_years, education
- EmployerProfile: company_name, company_description, website

---

## Completed Features (Phase 2)

### Templates & Static Files
- templates/base.html - Base template with Bootstrap navbar, messages, footer
- templates/home.html - Landing page with feature cards, dynamic content based on auth
- templates/users/register_job_seeker.html - Job seeker registration form
- templates/users/register_employer.html - Employer registration form (includes company info)
- templates/users/login.html - Login form
- static/css/style.css - Custom styling

### URL Structure
- / - Home page
- /users/register/job-seeker/ - Job seeker registration
- /users/register/employer/ - Employer registration
- /users/login/ - Login
- /users/logout/ - Logout
- /admin/ - Django admin

### Views & Forms
users/views.py:
  - home() - Landing page
  - register_job_seeker() - Job seeker registration with auto-profile creation
  - register_employer() - Employer registration with company info
  - login_view() - Authentication
  - logout_view() - Session logout
  
users/forms.py:
  - JobSeekerRegistrationForm - Extends UserCreationForm, auto-creates JobSeekerProfile
  - EmployerRegistrationForm - Extends UserCreationForm, auto-creates EmployerProfile with company data

### Features Working
- User registration with validation (password strength, email format, etc.)
- Automatic profile creation on signup
- Login/logout with session management
- Success/error messages (Django messages framework)
- Role detection (user_type displayed in navbar)
- Redirect logic (logged-in users can't access registration/login)
- Bootstrap 5 responsive design

---

## Next Steps: Complete Phase 2

### Task 4: Profile Pages (TODO)

Profile View (/users/profile/):
- Display user info (name, email, phone)
- Job Seeker: show resume, skills, experience, education
- Employer: show company name, description, website
- Different layouts based on user_type

Profile Edit (/users/profile/edit/):
- Forms to update user info
- Job Seeker: edit profile fields, upload resume
- Employer: edit company info
- File upload handling for resumes
- Success messages

### Task 5: Dashboards (TODO)

Job Seeker Dashboard (/users/dashboard/):
- Welcome message
- Stats: applications submitted, profile completion
- Recent jobs (placeholder)
- Quick actions (Browse Jobs, Edit Profile)

Employer Dashboard (/users/dashboard/):
- Welcome with company name
- Stats: jobs posted, applications received
- List of posted jobs
- Quick actions (Post Job, View Applications)

---

## Phase 3: Job Management (PLANNED)

For Employers:
- Post new jobs
- View/edit/delete their jobs
- View applications received

For Job Seekers:
- Browse all active jobs
- Search & filter jobs
- View job details
- Apply to jobs

---

## Phase 4: Application System (PLANNED)

- Job seekers apply to jobs
- Resume upload/attachment
- Employers review applications
- Status management (pending/reviewed/interview/rejected/accepted)
- Application tracking

---

## Phase 5: Polish & Enhancements (PLANNED)

- Email notifications
- Advanced search & filters
- Analytics for employers
- Better UI/UX styling
- Profile pictures

---

## Development Workflow

Activate virtual environment:
source venv/bin/activate

Run migrations (if models changed):
python manage.py makemigrations
python manage.py migrate

Run development server:
python manage.py runserver

Access URLs:
- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin
- Login: http://127.0.0.1:8000/users/login/

---

## Project Structure

jobportal/
├── manage.py
├── db.sqlite3
├── config/
│   ├── settings.py
│   ├── urls.py          # Main URL config, includes users & jobs apps
│   └── wsgi.py
├── users/
│   ├── models.py        # User, JobSeekerProfile, EmployerProfile
│   ├── views.py         # Registration, login, logout views
│   ├── forms.py         # Registration forms
│   ├── urls.py          # User-related URL patterns
│   └── admin.py         # Admin config
├── jobs/
│   ├── models.py        # Job, Application models
│   ├── urls.py          # Empty for now
│   └── admin.py
├── companies/           # Empty for now
├── templates/
│   ├── base.html        # Base template with navbar
│   ├── home.html        # Landing page
│   └── users/
│       ├── register_job_seeker.html
│       ├── register_employer.html
│       └── login.html
├── static/
│   └── css/
│       └── style.css    # Custom styling
└── venv/                # Virtual environment

---

## Testing Checklist

Registration:
- Job seeker registration creates User + JobSeekerProfile
- Employer registration creates User + EmployerProfile + company info
- Password validation working
- Duplicate username prevented
- Email validation working

Authentication:
- Login works with username/password
- Logout destroys session
- Success/error messages display
- Redirects work (logged-in users redirected to home)
- Navbar updates based on auth state

UI/UX:
- Bootstrap styling applied
- Responsive design works
- Forms have proper validation feedback
- Navigation links work
- Messages auto-dismiss

---

## Notes
- Solo project for learning Django
- Mac-only development
- SQLite for simplicity
- Focus on functionality first, polish later
- Using Django's built-in authentication system
- Bootstrap 5 via CDN (no local files)

---

## Git Workflow

After completing a task:
git add .
git commit -m "Completed Phase 2 Task 3: Login/Logout"
git push origin main

---

## Known Issues / Future Improvements
- Add password reset functionality
- Add email verification
- Add "Remember me" on login
- Add profile pictures
- Add social auth (Google, LinkedIn)
