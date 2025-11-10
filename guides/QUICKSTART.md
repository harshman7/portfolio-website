# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Migrations
```bash
python manage.py migrate
```

### Step 3: Load Resume Data
```bash
python manage.py load_resume_data
```

### Step 4: Start the Server
```bash
python manage.py runserver
```

### Step 5: View Your Portfolio
Open your browser and visit: **http://127.0.0.1:8000/**

## 🎨 Features

✅ Modern, responsive design with Tailwind CSS  
✅ Fully populated with your resume data  
✅ Smooth scrolling and animations  
✅ Skills visualization  
✅ Work experience showcase  
✅ Projects portfolio  
✅ Certifications display  
✅ Admin panel for easy content management  

## 📝 Admin Panel

To access the admin panel and manage your content:

1. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

2. Visit: **http://127.0.0.1:8000/admin/**

3. Login and manage:
   - Profile information
   - Education
   - Skills
   - Work Experience
   - Projects
   - Certifications

## 🗄️ Database

By default, the project uses **SQLite** (no setup required!).

To use **PostgreSQL** instead:
1. Install PostgreSQL
2. Run: `./setup_postgres.sh`
3. Set environment variables (see README.md)
4. Restart the server

## 🎯 Next Steps

- Customize the design in `templates/portfolio/index.html`
- Add your profile image in the admin panel
- Update project images and links
- Add more skills, projects, or experiences
- Deploy to production (see README.md)

## ❓ Need Help?

Check the full README.md for detailed documentation.

