================================================================================
YOUR DJANGO JOB PORTAL DATABASE GUIDE
================================================================================

🗄️ DATABASE TYPE: SQLite
- File: db.sqlite3 (in project root)
- Type: File-based database (no server needed)
- Good for: Development, small projects
- Limitations: Not ideal for production/high-traffic sites

================================================================================
📋 DATABASE TABLES
================================================================================

1. USERS TABLE (users)
┌─────────────────┬──────────────┬─────────────────────┐
│ Field           │ Type         │ Description         │
├─────────────────┼──────────────┼─────────────────────┤
│ id              │ INT (PK)     │ Auto-increment ID   │
│ username        │ VARCHAR      │ Unique username     │
│ email           │ VARCHAR      │ Email address       │
│ password        │ VARCHAR      │ Hashed password     │
│ first_name      │ VARCHAR(30)  │ First name          │
│ last_name       │ VARCHAR(30)  │ Last name           │
│ user_type       │ VARCHAR(20)  │ 'job_seeker' or     │
│                 │              │ 'employer'          │
│ phone           │ VARCHAR(15)  │ Phone number        │
│ created_at      │ DATETIME     │ Registration date   │
│ is_active       │ BOOLEAN      │ Account active?     │
│ is_staff        │ BOOLEAN      │ Admin access?       │
│ is_superuser    │ BOOLEAN      │ Superuser?          │
└─────────────────┴──────────────┴─────────────────────┘

2. JOB SEEKER PROFILES TABLE (job_seeker_profiles)
┌──────────────────┬─────────────┬────────────────────┐
│ Field            │ Type        │ Description        │
├──────────────────┼─────────────┼────────────────────┤
│ id               │ INT (PK)    │ Auto-increment ID  │
│ user_id          │ INT (FK)    │ → users.id         │
│ resume           │ VARCHAR     │ File path          │
│ skills           │ TEXT        │ Skills list        │
│ experience_years │ INT         │ Years of exp.      │
│ education        │ VARCHAR(200)│ Education info     │
└──────────────────┴─────────────┴────────────────────┘

3. EMPLOYER PROFILES TABLE (employer_profiles)
┌─────────────────────┬─────────────┬────────────────────┐
│ Field               │ Type        │ Description        │
├─────────────────────┼─────────────┼────────────────────┤
│ id                  │ INT (PK)    │ Auto-increment ID  │
│ user_id             │ INT (FK)    │ → users.id         │
│ company_name        │ VARCHAR(200)│ Company name       │
│ company_description │ TEXT        │ Company info       │
│ website             │ VARCHAR     │ Company URL        │
└─────────────────────┴─────────────┴────────────────────┘

4. JOBS TABLE (jobs)
┌──────────────┬──────────────┬───────────────────────┐
│ Field        │ Type         │ Description           │
├──────────────┼──────────────┼───────────────────────┤
│ id           │ INT (PK)     │ Auto-increment ID     │
│ employer_id  │ INT (FK)     │ → users.id (employer) │
│ title        │ VARCHAR(200) │ Job title             │
│ description  │ TEXT         │ Job description       │
│ requirements │ TEXT         │ Job requirements      │
│ location     │ VARCHAR(200) │ Job location          │
│ job_type     │ VARCHAR(20)  │ 'full_time',          │
│              │              │ 'part_time', etc.     │
│ salary_min   │ DECIMAL(10,2)│ Min salary (optional) │
│ salary_max   │ DECIMAL(10,2)│ Max salary (optional) │
│ is_active    │ BOOLEAN      │ Job active?           │
│ created_at   │ DATETIME     │ Posted date           │
│ updated_at   │ DATETIME     │ Last modified         │
└──────────────┴──────────────┴───────────────────────┘

5. APPLICATIONS TABLE (applications)
┌──────────────┬─────────────┬───────────────────────┐
│ Field        │ Type        │ Description           │
├──────────────┼─────────────┼───────────────────────┤
│ id           │ INT (PK)    │ Auto-increment ID     │
│ job_id       │ INT (FK)    │ → jobs.id             │
│ applicant_id │ INT (FK)    │ → users.id (job seeker)│
│ cover_letter │ TEXT        │ Cover letter          │
│ status       │ VARCHAR(20) │ 'pending', 'reviewed',│
│              │             │ 'interview', etc.     │
│ applied_at   │ DATETIME    │ Application date      │
└──────────────┴─────────────┴───────────────────────┘
UNIQUE CONSTRAINT: (job_id, applicant_id) → Prevents duplicate applications

================================================================================
🔗 TABLE RELATIONSHIPS
================================================================================

users (User)
  │
  ├─── OneToOne ──→ job_seeker_profiles (JobSeekerProfile)
  │                  (if user_type = 'job_seeker')
  │
  ├─── OneToOne ──→ employer_profiles (EmployerProfile)
  │                  (if user_type = 'employer')
  │
  ├─── ForeignKey ──→ jobs (Job)
  │                   (employer creates many jobs)
  │
  └─── ForeignKey ──→ applications (Application)
                      (job seeker creates many applications)

jobs (Job)
  │
  └─── ForeignKey ──→ applications (Application)
                      (one job has many applications)

================================================================================
🔍 KEY DATABASE CONCEPTS
================================================================================

PRIMARY KEYS (PK)
- Every table has an 'id' field
- Auto-increments: 1, 2, 3, 4...
- Uniquely identifies each row

FOREIGN KEYS (FK)
- Links tables together
- Example: employer_id in jobs table points to id in users table
- on_delete=CASCADE means: if user is deleted, their jobs are also deleted

ONETOONE RELATIONSHIPS
- Each user has exactly ONE profile
- Example: User #5 → JobSeekerProfile #5

FOREIGNKEY (One-to-Many)
- One employer can have many jobs
- One job can have many applications
- Example: Employer #3 → Job #10, Job #11, Job #12

UNIQUE CONSTRAINTS
- (job_id, applicant_id) in applications table
- Prevents: User #5 applying to Job #10 twice

================================================================================
💾 EXAMPLE DATA FLOW
================================================================================

WHEN A JOB SEEKER REGISTERS:
1. Creates row in 'users' table (id=1, user_type='job_seeker')
2. Automatically creates row in 'job_seeker_profiles' (id=1, user_id=1)

WHEN AN EMPLOYER POSTS A JOB:
1. Creates row in 'jobs' table (id=1, employer_id=2)

WHEN A JOB SEEKER APPLIES:
1. Creates row in 'applications' table (id=1, job_id=1, applicant_id=1)

WHEN YOU QUERY "Show all applications for Job #1":
Application.objects.filter(job_id=1)
Returns all rows in 'applications' where job_id=1

================================================================================
🛠️ DJANGO MIGRATIONS (Database Changes)
================================================================================

CREATE MIGRATION FILES (blueprints for database changes):
python manage.py makemigrations

APPLY MIGRATIONS (actually change the database):
python manage.py migrate

WHAT HAPPENS:
1. Django looks at your models (models.py)
2. Compares to current database structure
3. Creates SQL commands to update database
4. Executes those SQL commands

MIGRATION FILES (in users/migrations/ and jobs/migrations/):
- Store history of all database changes
- Like "git commits" for your database
- Example: 0001_initial.py, 0002_add_phone_field.py

RUN THESE COMMANDS WHENEVER YOU CHANGE models.py

================================================================================
📂 WHERE DATA IS STORED
================================================================================

SQLITE DATABASE FILE:
- Location: db.sqlite3 (in project root)
- Format: Binary file (can't read with text editor)
- Size: Grows as you add data

UPLOADED FILES (Resumes):
- Location: media/resumes/ folder
- Database stores: File path (e.g., "resumes/resume_2024.pdf")
- Actual file: Stored in filesystem, not database

================================================================================
🔧 INTERACTING WITH DATABASE - DJANGO ORM
================================================================================

You don't write SQL - Django does it for you!

GET ALL JOBS:
jobs = Job.objects.all()

GET SPECIFIC JOB:
job = Job.objects.get(id=1)

FILTER JOBS:
jobs = Job.objects.filter(job_type='full_time')

CREATE NEW JOB:
job = Job.objects.create(
    employer=user,
    title="Software Developer",
    description="Great opportunity..."
)

UPDATE JOB:
job.title = "Senior Software Developer"
job.save()

DELETE JOB:
job.delete()

BEHIND THE SCENES, DJANGO CONVERTS TO SQL:
Job.objects.all() → SELECT * FROM jobs;
Job.objects.filter(job_type='full_time') → SELECT * FROM jobs WHERE job_type = 'full_time';

================================================================================
🔍 VIEWING YOUR ACTUAL DATA
================================================================================

OPTION 1: DJANGO ADMIN (Easiest)
python manage.py runserver
Visit: http://127.0.0.1:8000/admin/

OPTION 2: DB BROWSER FOR SQLite (Visual Tool)
Download: https://sqlitebrowser.org/
Open db.sqlite3 file
Browse tables visually

OPTION 3: DJANGO SHELL (Command Line)
python manage.py shell

from users.models import User
from jobs.models import Job, Application

# How many users?
print(User.objects.count())

# List all jobs
for job in Job.objects.all():
    print(f"{job.title} - {job.employer.username}")

# How many applications total?
print(Application.objects.count())

================================================================================
⚠️ IMPORTANT DATABASE NOTES
================================================================================

DATA PERSISTENCE:
- Data stays in db.sqlite3 even when server stops
- Deleting db.sqlite3 = ALL DATA LOST
- Always backup before major changes

WHEN TO MAKE MIGRATIONS:
Run these commands whenever you change models.py:
python manage.py makemigrations
python manage.py migrate

SQLITE LIMITATIONS:
✅ Great for development
✅ Easy setup (no server needed)
⚠️ Single file (can corrupt)
⚠️ Not for production/high traffic
⚠️ Limited concurrent writes

FOR PRODUCTION, SWITCH TO:
- PostgreSQL (recommended)
- MySQL
- Oracle

================================================================================
📊 USEFUL DJANGO SHELL COMMANDS
================================================================================

START SHELL:
python manage.py shell

BASIC QUERIES:
from users.models import User
from jobs.models import Job, Application

# Count all users
User.objects.count()

# Count job seekers
User.objects.filter(user_type='job_seeker').count()

# Count employers
User.objects.filter(user_type='employer').count()

# Count all jobs
Job.objects.count()

# Count active jobs
Job.objects.filter(is_active=True).count()

# Count all applications
Application.objects.count()

# Count pending applications
Application.objects.filter(status='pending').count()

# Get all jobs for a specific employer
employer = User.objects.get(username='employer1')
Job.objects.filter(employer=employer)

# Get all applications for a specific job
job = Job.objects.get(id=1)
Application.objects.filter(job=job)

# Get all applications by a job seeker
seeker = User.objects.get(username='jobseeker1')
Application.objects.filter(applicant=seeker)

================================================================================
💾 BACKUP AND RESET
================================================================================

BACKUP DATABASE:
cp db.sqlite3 db.sqlite3.backup

RESTORE FROM BACKUP:
cp db.sqlite3.backup db.sqlite3

RESET DATABASE (DELETE ALL DATA):
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser

EXPORT DATA (JSON):
python manage.py dumpdata > backup.json

IMPORT DATA (JSON):
python manage.py loaddata backup.json

================================================================================
END OF DATABASE GUIDE
================================================================================