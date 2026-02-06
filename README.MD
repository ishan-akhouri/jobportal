# Django Job Portal

A full-featured job board web application built with Django 6.0 and SQLite. This platform connects job seekers with employers, allowing job seekers to browse and apply for positions while employers can post jobs and review applications.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey)

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### For Job Seekers
- ✅ User registration and authentication
- ✅ Profile management with resume upload
- ✅ Browse and search job listings
- ✅ Filter jobs by location and job type
- ✅ View detailed job descriptions
- ✅ Apply to jobs with cover letters
- ✅ Track application status
- ✅ View application history
- ✅ Personalized dashboard with statistics

### For Employers
- ✅ Company profile creation
- ✅ Post new job openings
- ✅ Edit and delete job postings
- ✅ View all posted jobs
- ✅ Review job applications
- ✅ Access applicant profiles and resumes
- ✅ Download candidate resumes
- ✅ Contact applicants via email
- ✅ Dashboard with application metrics

### General Features
- ✅ Role-based access control (Job Seekers vs Employers)
- ✅ Responsive Bootstrap 5 UI
- ✅ Form validation and error handling
- ✅ Success/error messaging system
- ✅ File upload functionality
- ✅ Duplicate application prevention
- ✅ Clean, intuitive user interface

## 🎥 Demo

### Live Demo
*Coming soon - Deployment in progress*

### Local Demo
```bash
# Clone and run locally (see Installation section)
python manage.py runserver
# Visit: http://127.0.0.1:8000
```

## 🛠️ Tech Stack

### Backend
- **Python 3.13** - Programming language
- **Django 6.0** - Web framework
- **SQLite** - Database (development)

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling
- **Bootstrap 5.3** - CSS framework
- **JavaScript** - Client-side functionality

### Additional Tools
- **Django ORM** - Database management
- **Django Forms** - Form handling and validation
- **Django Admin** - Administrative interface

## 📁 Project Structure

```
job_portal/
├── config/                 # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
│
├── users/                  # User management app
│   ├── models.py          # User, JobSeekerProfile, EmployerProfile
│   ├── views.py           # Authentication, profiles, dashboards
│   ├── forms.py           # Registration and profile forms
│   ├── urls.py            # User-related URLs
│   └── migrations/        # Database migrations
│
├── jobs/                   # Job management app
│   ├── models.py          # Job, Application models
│   ├── views.py           # Job CRUD, applications
│   ├── forms.py           # Job posting, application forms
│   ├── urls.py            # Job-related URLs
│   └── migrations/        # Database migrations
│
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── home.html          # Landing page
│   ├── users/             # User templates
│   │   ├── login.html
│   │   ├── register_*.html
│   │   ├── profile*.html
│   │   └── dashboard_*.html
│   └── jobs/              # Job templates
│       ├── job_list.html
│       ├── job_detail.html
│       ├── apply.html
│       └── my_*.html
│
├── static/                 # Static files
│   └── css/
│       └── style.css      # Custom CSS
│
├── media/                  # User uploads
│   └── resumes/           # Resume files
│
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── README.md              # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.13 or higher
- pip (Python package manager)
- Git

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/ishanakhouri/jobportal.git
cd jobportal
```

2. **Create a virtual environment**
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install django==6.0
```

4. **Apply database migrations**
```bash
python manage.py migrate
```

5. **Create a superuser (for admin access)**
```bash
python manage.py createsuperuser
# Follow prompts to set username, email, and password
```

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Main site: http://127.0.0.1:8000
- Admin panel: http://127.0.0.1:8000/admin

## 📖 Usage

### For Job Seekers

1. **Register an account**
   - Go to homepage
   - Click "Register as Job Seeker"
   - Fill in your details
   - Login with your credentials

2. **Complete your profile**
   - Navigate to Profile → Edit Profile
   - Upload your resume
   - Add skills, education, and experience

3. **Browse and apply for jobs**
   - Click "Jobs" in navigation
   - Use search and filters to find relevant positions
   - Click on a job to view details
   - Click "Apply Now" and submit your application with a cover letter

4. **Track your applications**
   - Go to Dashboard
   - Click "My Applications"
   - View status of all submitted applications

### For Employers

1. **Register a company account**
   - Go to homepage
   - Click "Register as Employer"
   - Provide company information
   - Login with your credentials

2. **Post a job**
   - Go to Dashboard
   - Click "Post a New Job"
   - Fill in job details (title, description, requirements, location, salary)
   - Submit to publish

3. **Manage job postings**
   - Navigate to "My Jobs"
   - View all your posted jobs
   - Edit or delete jobs as needed

4. **Review applications**
   - In "My Jobs", click "View Applications"
   - Review applicant profiles and cover letters
   - Download resumes
   - Contact candidates via email

### Admin Access

1. **Access admin panel**
   - Go to http://127.0.0.1:8000/admin
   - Login with superuser credentials

2. **Manage data**
   - View and edit all users, jobs, and applications
   - Manage user permissions
   - Delete spam or inappropriate content

## 🗄️ Database Schema

### Tables

**users** - User accounts
- id, username, email, password, first_name, last_name
- user_type (job_seeker | employer)
- phone, created_at, is_active

**job_seeker_profiles** - Job seeker information
- id, user_id (FK)
- resume, skills, experience_years, education

**employer_profiles** - Company information
- id, user_id (FK)
- company_name, company_description, website

**jobs** - Job postings
- id, employer_id (FK)
- title, description, requirements, location
- job_type, salary_min, salary_max
- is_active, created_at, updated_at

**applications** - Job applications
- id, job_id (FK), applicant_id (FK)
- cover_letter, status, applied_at
- UNIQUE constraint: (job_id, applicant_id)

### Relationships

```
User (1) ←→ (1) JobSeekerProfile  [OneToOne]
User (1) ←→ (1) EmployerProfile   [OneToOne]
User (1) ←→ (N) Job                [ForeignKey - employer]
User (1) ←→ (N) Application        [ForeignKey - applicant]
Job  (1) ←→ (N) Application        [ForeignKey]
```

For detailed database documentation, see [database.md](database.md)

## 📸 Screenshots

### Homepage
*Screenshot coming soon*

### Job Listing
*Screenshot coming soon*

### Job Detail & Application
*Screenshot coming soon*

### Employer Dashboard
*Screenshot coming soon*

### Job Seeker Dashboard
*Screenshot coming soon*

## 🎯 Future Enhancements

### Phase 4: Advanced Features
- [ ] Application status updates (reviewed, interview, accepted, rejected)
- [ ] Email notifications for status changes
- [ ] Advanced search with salary range filter
- [ ] Pagination for job listings
- [ ] Save/bookmark favorite jobs
- [ ] Job expiration dates
- [ ] Featured/promoted job listings

### Phase 5: Polish & Production
- [ ] Unit and integration tests
- [ ] API endpoints (REST API)
- [ ] Password reset functionality
- [ ] Profile pictures and company logos
- [ ] Social media sharing
- [ ] Analytics dashboard for employers
- [ ] PostgreSQL migration for production
- [ ] Docker containerization
- [ ] Cloud deployment (AWS/Heroku)

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
# After modifying models.py
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

### Database Backup
```bash
# Backup
cp db.sqlite3 db.sqlite3.backup

# Restore
cp db.sqlite3.backup db.sqlite3
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

### Coding Standards
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Write docstrings for functions and classes
- Test your changes before submitting

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Ishan Akhouri**
- GitHub: [@ishan-akhouri](https://github.com/ishan-akhouri)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Documentation
- Stack Overflow community
- Claude AI for development assistance

## 📞 Support

If you have any questions or run into issues:
- Open an issue on GitHub
- Email me

---

**Built with ❤️ using Django**