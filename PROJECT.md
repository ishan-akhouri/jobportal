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

## Current Status: Phase 2 Complete! ✅

### Phase 1: Complete ✅
- Django project structure
- Custom User model (job_seeker/employer types)
- Job model (posting details)
- Application model (job applications)
- JobSeekerProfile & EmployerProfile models
- Admin interface configured
- Database migrations working

### Phase 2: Authentication & User Management ✅ (100% COMPLETE)
- ✅ Task 1: URL structure & templates setup
- ✅ Task 2: Registration system (job seekers & employers)
- ✅ Task 3: Login/logout functionality
- ✅ Task 4: Profile pages (view & edit)
- ✅ Task 5: Role-based dashboards

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

## Completed Features (Phase 2) ✅

### Templates & Static Files
- templates/base.html - Base template with Bootstrap navbar, messages, footer
- templates/home.html - Landing page with feature cards, dynamic content based on auth
- templates/users/register_job_seeker.html - Job seeker registration form
- templates/users/register_employer.html - Employer registration form (includes company info)
- templates/users/login.html - Login form
- templates/users/profile.html - Profile view page (conditional for job seeker/employer)
- templates/users/profile_edit.html - Profile edit form with file uploads
- templates/users/dashboard_job_seeker.html - Job seeker dashboard with stats
- templates/users/dashboard_employer.html - Employer dashboard with job listings
- static/css/style.css - Custom styling

### URL Structure
- / - Home page
- /users/register/job-seeker/ - Job seeker registration
- /users/register/employer/ - Employer registration
- /users/login/ - Login (redirects to dashboard)
- /users/logout/ - Logout
- /users/profile/ - View profile (read-only)
- /users/profile/edit/ - Edit profile (with file upload)
- /users/dashboard/ - Role-based dashboard (routes to correct dashboard)
- /admin/ - Django admin

### Views & Forms
users/views.py:
  - home() - Landing page with dynamic content
  - register_job_seeker() - Job seeker registration with auto-profile creation
  - register_employer() - Employer registration with company info
  - login_view() - Authentication, redirects to dashboard
  - logout_view() - Session logout
  - profile_view() - Display profile (different layouts for job seeker/employer)
  - profile_edit_view() - Edit profile with file upload support
  - dashboard_view() - Routes to appropriate dashboard based on user_type
  
users/forms.py:
  - JobSeekerRegistrationForm - Extends UserCreationForm, auto-creates JobSeekerProfile
  - EmployerRegistrationForm - Extends UserCreationForm, auto-creates EmployerProfile with company data
  - JobSeekerProfileEditForm - Edit job seeker profile + user fields, handles resume upload
  - EmployerProfileEditForm - Edit employer profile + user fields, handles company info

### Features Working ✅
- User registration with validation (password strength, email format, etc.)
- Automatic profile creation on signup
- Login/logout with session management
- Success/error messages (Django messages framework)
- Role detection (user_type displayed in navbar)
- Redirect logic (logged-in users redirect to dashboard)
- Profile viewing (read-only display)
- Profile editing (with form validation)
- Resume file uploads (for job seekers)
- Profile completion percentage calculation
- Role-based dashboards:
  - Job seeker: shows applications count, profile completion %, experience
  - Employer: shows jobs posted count, applications received count
- Database queries for stats (applications, jobs)
- Auto-profile creation if missing
- Bootstrap 5 responsive design
- Proper file handling for media uploads

---

## Next Phase: Phase 3 - Job Management (PLANNED)

### For Employers:
- ✏️ Create job posting form
- 📝 Post new jobs
- 📋 View all posted jobs (list page)
- ✏️ Edit existing jobs
- 🗑️ Delete jobs
- 👀 View applications for each job

### For Job Seekers:
- 🔍 Browse all available jobs (job listing page)
- 🔎 Search & filter jobs (by title, location, type)
- 👁️ View job details (individual job page)
- 📄 Apply to jobs (application form with cover letter)
- 📋 View application history ("My Applications" page)
- ❌ Withdraw applications

### What We'll Build in Phase 3:
1. Job listing page (browse all jobs)
2. Job detail page (individual job view)
3. Job application form (apply with cover letter)
4. Job posting form (for employers)
5. Job management pages (employer can edit/delete)
6. Application tracking (job seekers see their applications)
7. Application management (employers review applications)

---

## Phase 4: Advanced Features (PLANNED)

Search & Filtering:
- Advanced job search with multiple criteria
- Filter by salary range, experience level, job type
- Sort by date posted, relevance, salary

Notifications:
- Email notifications for new applications
- Email alerts for job seekers when new jobs match profile

Application Status Management:
- Employers update status (pending, reviewed, accepted, rejected)
- Job seekers see application status
- Status change notifications

Saved Jobs:
- Job seekers can save/bookmark jobs
- View saved jobs list
- Quick apply to saved jobs

Company Profiles:
- Public company pages
- View all jobs from specific company
- Company ratings/reviews

---

## Phase 5: Polish & Deployment (PLANNED)

UI/UX Improvements:
- Enhanced styling and animations
- Loading states for async operations
- Better error handling and user feedback
- Mobile responsiveness optimization

Security:
- Rate limiting for forms
- Enhanced input validation
- SQL injection prevention (Django ORM handles this)
- XSS protection

Performance:
- Database query optimization
- Pagination for job listings
- Caching for frequently accessed data
- Image optimization for company logos

Deployment:
- Production settings configuration
- Deploy to hosting platform (Heroku, Railway, etc.)
- Set up PostgreSQL for production
- Configure static files and media uploads for production
- Domain name and SSL certificate

---

## Development Workflow

Activate virtual environment:
```bash
source venv/bin/activate
```

Run migrations (if models changed):
```bash
python manage.py makemigrations
python manage.py migrate
```

Run development server:
```bash
python manage.py runserver
```

Access URLs:
- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin
- Login: http://127.0.0.1:8000/users/login/
- Dashboard: http://127.0.0.1:8000/users/dashboard/
- Profile: http://127.0.0.1:8000/users/profile/

---

## Project Structure

```
jobportal/
├── manage.py
├── db.sqlite3
├── PROJECT.md
├── config/
│   ├── settings.py
│   ├── urls.py          # Main URL config, includes users & jobs apps
│   └── wsgi.py
├── users/
│   ├── models.py        # User, JobSeekerProfile, EmployerProfile
│   ├── views.py         # All user views including dashboard
│   ├── forms.py         # Registration & profile edit forms
│   ├── urls.py          # User-related URL patterns
│   └── admin.py         # Admin config
├── jobs/
│   ├── models.py        # Job, Application models
│   ├── urls.py          # Empty for now (Phase 3)
│   └── admin.py
├── companies/           # Empty for now
├── templates/
│   ├── base.html        # Base template with navbar
│   ├── home.html        # Landing page
│   └── users/
│       ├── register_job_seeker.html
│       ├── register_employer.html
│       ├── login.html
│       ├── profile.html
│       ├── profile_edit.html
│       ├── dashboard_job_seeker.html
│       └── dashboard_employer.html
├── static/
│   └── css/
│       └── style.css    # Custom styling
├── media/              # User uploaded files (resumes)
│   └── resumes/
└── venv/               # Virtual environment
```

---

## Testing Checklist (Phase 2) ✅

### Registration:
- ✅ Job seeker registration creates User + JobSeekerProfile
- ✅ Employer registration creates User + EmployerProfile + company info
- ✅ Password validation working
- ✅ Duplicate username prevented
- ✅ Email validation working

### Authentication:
- ✅ Login works with username/password
- ✅ Login redirects to dashboard
- ✅ Logout destroys session
- ✅ Success/error messages display
- ✅ Redirects work (logged-in users redirected appropriately)
- ✅ Navbar updates based on auth state

### Profile Management:
- ✅ Profile view displays correct information
- ✅ Different layouts for job seeker vs employer
- ✅ Profile edit form pre-populates data
- ✅ Profile updates save correctly
- ✅ Resume upload works
- ✅ Resume replacement works
- ✅ Success messages after profile update
- ✅ Validation on profile forms

### Dashboards:
- ✅ Job seeker dashboard shows correct stats
- ✅ Employer dashboard shows correct stats
- ✅ Profile completion percentage calculates correctly
- ✅ Dashboard routes based on user_type
- ✅ Quick action buttons work
- ✅ Placeholders for future features display correctly

### UI/UX:
- ✅ Bootstrap styling applied everywhere
- ✅ Responsive design works
- ✅ Forms have proper validation feedback
- ✅ Navigation links work
- ✅ Messages display and auto-dismiss
- ✅ Emojis display correctly (UTF-8 encoding)

---

## Progress Tracker

```
Phase 1: ████████████████████ 100% ✅ COMPLETE
Phase 2: ████████████████████ 100% ✅ COMPLETE
Phase 3: ░░░░░░░░░░░░░░░░░░░░   0% 🚧 NEXT UP
Phase 4: ░░░░░░░░░░░░░░░░░░░░   0% 
Phase 5: ░░░░░░░░░░░░░░░░░░░░   0%

Overall: ████████░░░░░░░░░░░░ 40% Complete
```

---

## Git Workflow

After completing a phase/task:
```bash
git add .
git commit -m "Completed Phase 2: Authentication & User Management"
git push origin main
```

---

## Known Issues / Future Improvements
- Add password reset functionality
- Add email verification
- Add "Remember me" on login
- Add profile pictures
- Add social auth (Google, LinkedIn)
- Improve emoji rendering consistency across browsers
- Add more detailed error messages
- Add loading indicators for file uploads

---

## Notes
- Solo project for learning Django
- Mac-only development
- SQLite for simplicity during development
- Focus on functionality first, polish later
- Using Django's built-in authentication system
- Bootstrap 5 via CDN (no local files)
- File uploads configured with MEDIA_ROOT and MEDIA_URL
- UTF-8 encoding configured for proper emoji display
- Following Django best practices throughout

---

## Lessons Learned (Phase 2)
- Always check model field names before querying (applicant vs job_seeker)
- UTF-8 encoding must be consistent across all files
- File upload forms need `enctype="multipart/form-data"`
- Profile auto-creation prevents missing profile errors
- Django's login_required decorator simplifies access control
- Bootstrap 5 makes responsive design much easier
- Success messages improve user experience significantly
- Methodical testing after each task catches issues early