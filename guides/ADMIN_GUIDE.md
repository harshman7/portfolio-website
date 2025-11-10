# Django Admin Panel Guide

## 🎯 Overview

The Django admin panel provides a user-friendly interface to manage all your portfolio content without writing code. This guide will help you set up and use the admin panel effectively.

## 🚀 Setup

### Step 1: Create a Superuser

To access the admin panel, you need to create a superuser account:

```bash
cd "/Users/harshmanpreetsingh/Desktop/Portfolio website"
python manage.py createsuperuser
```

You'll be prompted to enter:
- **Username**: Choose a username (e.g., `admin`)
- **Email**: Enter your email address (optional)
- **Password**: Enter a secure password (you'll need to confirm it)

### Step 2: Start the Development Server

```bash
python manage.py runserver
```

### Step 3: Access the Admin Panel

1. Open your browser
2. Navigate to: **http://127.0.0.1:8000/admin/**
3. Login with your superuser credentials

## 📋 Admin Panel Features

### Dashboard

The admin dashboard shows:
- **Portfolio** section with all your models
- Quick access to add/edit content
- Recent actions log

### Available Models

#### 1. **Profile**
Manage your personal information:
- Full name
- Location
- Phone number
- Email address
- Bio/About me
- Profile image (upload)

**How to use:**
- Click "Profiles" → "Add Profile" or edit existing
- Upload a profile image (recommended: square image, 400x400px or larger)
- Fill in your contact information
- Save changes

#### 2. **Education**
Manage your educational background:
- Institution name
- Location
- Degree
- Major
- Graduation date
- GPA
- Description
- Display order

**How to use:**
- Click "Educations" → "Add Education"
- Fill in your education details
- Set the order (lower numbers appear first)
- Save changes

#### 3. **Skills**
Manage your technical skills:
- Skill name
- Category (Frontend, Backend, Database, Cloud, Tools, Other)
- Proficiency level (1-5)
- Display order

**How to use:**
- Click "Skills" → "Add Skill"
- Enter skill name (e.g., "Python", "React")
- Select category
- Set proficiency (1 = beginner, 5 = expert)
- Set display order
- Save changes

**Tip**: Skills are grouped by category on your portfolio website.

#### 4. **Work Experience**
Manage your work history:
- Company name
- Location
- Position/Job title
- Start date
- End date (or mark as current)
- Description
- Achievements (JSON array)
- Display order

**How to use:**
- Click "Work Experiences" → "Add Work Experience"
- Fill in company and position details
- Enter dates (format: "May 2023" or "Jan 2024")
- Mark "Is current" if this is your current job
- Write a description of your role
- Add achievements as a JSON array: `["Achievement 1", "Achievement 2"]`
- Set display order (most recent first)
- Save changes

**Example achievements JSON:**
```json
[
  "Led team of 5 developers",
  "Improved performance by 30%",
  "Implemented new features"
]
```

#### 5. **Projects**
Manage your portfolio projects:
- Project title
- Project date
- Description
- Tech stack (comma-separated)
- Features (JSON array)
- GitHub URL
- Live URL
- Project image
- Display order

**How to use:**
- Click "Projects" → "Add Project"
- Enter project title and date
- Write a compelling description
- List technologies: `Python, Django, PostgreSQL, Tailwind CSS`
- Add features as JSON array
- Add GitHub and live demo URLs (if available)
- Upload a project screenshot/image
- Set display order
- Save changes

**Example tech stack:**
```
Python, Django, PostgreSQL, Tailwind CSS, Docker
```

**Example features JSON:**
```json
[
  "User authentication",
  "Real-time updates",
  "Responsive design"
]
```

#### 6. **Certifications**
Manage your certifications:
- Certification name
- Issuer (e.g., "AWS", "Google Cloud")
- Issue date
- Expiry date (if applicable)
- Credential ID
- Credential URL
- Display order

**How to use:**
- Click "Certifications" → "Add Certification"
- Enter certification details
- Add credential URL if you have a verification link
- Set display order
- Save changes

## 🎨 Tips and Best Practices

### 1. **Profile Image**
- Use a professional headshot
- Recommended size: 400x400px or larger
- Square images work best
- Supported formats: JPG, PNG, GIF

### 2. **Project Images**
- Use high-quality screenshots
- Recommended size: 1200x600px or larger
- Show your project's key features
- Supported formats: JPG, PNG, GIF

### 3. **Display Order**
- Lower numbers appear first
- For work experience: Use descending order (10, 9, 8...) so most recent appears first
- For skills: Group by category, then order within category

### 4. **Dates Format**
- Use consistent format: "Month Year" (e.g., "May 2023", "Jan 2024")
- For current positions: Leave end date empty and check "Is current"

### 5. **JSON Arrays**
- Use proper JSON format: `["Item 1", "Item 2", "Item 3"]`
- Each item should be in quotes
- Separate items with commas
- No trailing comma after last item

### 6. **Tech Stack**
- Comma-separated list: `Python, Django, PostgreSQL`
- Use consistent naming (e.g., "JavaScript" not "JS")
- List technologies in order of importance/relevance

## 🔍 Searching and Filtering

### Search
- Use the search box to find specific items
- Search works on relevant fields (name, title, description, etc.)

### Filters
- Use filters to narrow down results
- Filter by category, date, status, etc.
- Multiple filters can be combined

### Bulk Actions
- Select multiple items using checkboxes
- Perform bulk actions (delete, etc.)
- Useful for managing large lists

## 📸 Adding Images

### Profile Image
1. Click on "Profile" in admin
2. Click "Choose File" next to "Profile image"
3. Select your image file
4. Click "Save"

### Project Images
1. Click on "Projects" in admin
2. Click on a project or create a new one
3. Click "Choose File" next to "Image"
4. Select your project screenshot
5. Click "Save"

## 🔄 Updating Content

### Edit Existing Content
1. Navigate to the model (e.g., "Projects")
2. Click on the item you want to edit
3. Make your changes
4. Click "Save" or "Save and continue editing"

### Delete Content
1. Navigate to the model
2. Select the item(s) you want to delete
3. Choose "Delete selected [items]" from the action dropdown
4. Click "Go" and confirm deletion

## 🎯 Common Tasks

### Adding a New Skill
1. Go to Admin → Skills → Add Skill
2. Enter skill name (e.g., "TypeScript")
3. Select category (e.g., "Frontend")
4. Set proficiency (1-5)
5. Set order
6. Save

### Adding a New Project
1. Go to Admin → Projects → Add Project
2. Enter title and description
3. Add tech stack (comma-separated)
4. Add features (JSON array)
5. Upload project image
6. Add GitHub/live URLs
7. Set order
8. Save

### Updating Work Experience
1. Go to Admin → Work Experiences
2. Click on the experience to edit
3. Update dates, description, or achievements
4. Save changes

## 🛠️ Troubleshooting

### Can't Login
- Make sure you created a superuser: `python manage.py createsuperuser`
- Check that the server is running: `python manage.py runserver`
- Verify you're using the correct URL: `http://127.0.0.1:8000/admin/`

### Images Not Showing
- Check that media files are being served (development mode)
- Verify image file format is supported (JPG, PNG, GIF)
- Check file size (large files may take time to upload)

### JSON Errors
- Make sure JSON arrays are properly formatted
- Use double quotes, not single quotes
- No trailing commas
- Valid JSON syntax

### Changes Not Reflecting
- Refresh your browser (Ctrl+F5 or Cmd+Shift+R)
- Clear browser cache
- Check that you clicked "Save"
- Verify the server is running

## 📚 Additional Resources

- [Django Admin Documentation](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
- [Django Models Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)

## 🎉 Quick Reference

**Admin URL**: http://127.0.0.1:8000/admin/

**Create Superuser**:
```bash
python manage.py createsuperuser
```

**Start Server**:
```bash
python manage.py runserver
```

**Models Available**:
- Profile
- Education
- Skills
- Work Experience
- Projects
- Certifications

---

Happy managing! 🚀

