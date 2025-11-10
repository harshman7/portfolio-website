# 🚀 Step-by-Step Deployment Guide - Render

## Deploy to Render (Free & Easy)

### Step 1: Prepare Your Code

```bash
# Make sure you're in the project directory
cd "/Users/harshmanpreetsingh/Desktop/Portfolio website"

# Initialize git if not already done
git init

# Add all files
git add .

# Commit
git commit -m "Portfolio website ready for deployment"
```

### Step 2: Push to GitHub

1. **Create a GitHub repository**
   - Go to https://github.com/new
   - Name: `portfolio-website` (or your preferred name)
   - Create repository

2. **Push your code**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/portfolio-website.git
   git branch -M main
   git push -u origin main
   ```

### Step 3: Deploy on Render

1. **Sign up for Render**
   - Go to https://render.com
   - Click "Get Started for Free"
   - Sign up with your GitHub account

2. **Create PostgreSQL Database**
   - In Render Dashboard, click "New +" → "PostgreSQL"
   - Name: `portfolio-db`
   - Plan: **Free**
   - Region: Choose closest to you
   - Click "Create Database"
   - **Wait for database to be created**
   - Go to database → "Connections" tab
   - **Copy the "Internal Database URL"** (you'll need this)

3. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub account (if not already)
   - Select your repository: `portfolio-website`
   - Click "Connect"

4. **Configure Web Service**
   - **Name**: `portfolio-website` (or your preferred name)
   - **Environment**: `Python 3`
   - **Region**: Same as database
   - **Branch**: `main`
   - **Root Directory**: (leave empty)
   - **Build Command**: 
     ```bash
     pip install -r requirements.txt && python manage.py collectstatic --noinput
     ```
   - **Start Command**: 
     ```bash
     gunicorn portfolio_project.wsgi:application
     ```
   - **Plan**: Free

5. **Set Environment Variables**
   - Click "Advanced" → "Add Environment Variable"
   - Add these variables:
     
     **SECRET_KEY**:
     ```bash
     # Generate in terminal:
     python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
     ```
     - Copy the generated key
     - Add as: `SECRET_KEY` = `(paste generated key)`
     
     **DEBUG**:
     - Name: `DEBUG`
     - Value: `False`
     
     **ALLOWED_HOSTS**:
     - Name: `ALLOWED_HOSTS`
     - Value: `portfolio-website.onrender.com` (or your service name)
     
     **DATABASE_URL**:
     - Name: `DATABASE_URL`
     - Value: `(paste the Internal Database URL from step 2)`

6. **Link Database (Optional but Recommended)**
   - In Web Service settings, go to "Environment" tab
   - Click "Link Database" → Select your PostgreSQL database
   - This automatically sets `DATABASE_URL`

7. **Deploy**
   - Click "Create Web Service"
   - Wait for build to complete (3-5 minutes)
   - Your site will be live at: `https://portfolio-website.onrender.com`

### Step 4: Setup Database

1. **Open Render Shell**
   - Go to your Web Service
   - Click "Shell" tab
   - Or use Render's console

2. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

3. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```
   - Enter username, email, and password

4. **Load Resume Data** (Optional)
   ```bash
   python manage.py load_resume_data
   ```

5. **Verify Deployment**
   - Visit: `https://portfolio-website.onrender.com`
   - Visit admin: `https://portfolio-website.onrender.com/admin`
   - Test all features

---

## Generate Secret Key

Run this command to generate a secure secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and use it as your `SECRET_KEY` environment variable.

---

## Environment Variables Summary

| Variable | Value | Where to Get |
|----------|-------|--------------|
| `SECRET_KEY` | Generated key | Run command above |
| `DEBUG` | `False` | Always `False` in production |
| `ALLOWED_HOSTS` | Your domain | Platform URL (e.g., `app.onrender.com`) |
| `DATABASE_URL` | Connection string | Internal Database URL from Render (or auto-set if linked) |

---

## Post-Deployment

### 1. Test Your Website
- Visit your live URL
- Check all sections load
- Test scroll animations
- Verify mobile responsiveness
- Test admin panel

### 2. Create Admin User
```bash
# In Render Shell:
python manage.py createsuperuser
```

### 3. Load Resume Data (Optional)
```bash
python manage.py load_resume_data
```

### 4. Customize Content
- Go to `/admin`
- Login with superuser credentials
- Update profile, projects, skills, etc.

---

## Troubleshooting

### Build Fails
- Check `requirements.txt` has all dependencies
- Verify Python version (3.11+)
- Check build logs for errors

### Static Files Not Loading
- Ensure `collectstatic` runs in build command
- Check WhiteNoise middleware is in `MIDDLEWARE`
- Verify `STATIC_ROOT` is set correctly

### Database Connection Error
- Check `DATABASE_URL` is set
- Verify PostgreSQL is running
- Check database credentials
- Verify database is linked to web service

### 500 Error
- Check `DEBUG=False` is set
- Verify `ALLOWED_HOSTS` includes your domain
- Check application logs
- Verify all environment variables are set

### Migration Errors
- Run `python manage.py migrate` in shell
- Check database connection
- Verify migrations are up to date

### Database Paused (Free Tier)
- Render free tier databases pause after 90 days of inactivity
- Resume database from Render dashboard
- Database will auto-resume when accessed

---

## Quick Deploy Script

```bash
#!/bin/bash
# Quick deploy to Render

# 1. Push to GitHub
git add .
git commit -m "Deploy to production"
git push origin main

# 2. Generate secret key
echo "Generate SECRET_KEY:"
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

echo ""
echo "✅ Code pushed to GitHub!"
echo "📋 Next steps:"
echo "1. Go to Render.com"
echo "2. Create PostgreSQL database"
echo "3. Create Web Service"
echo "4. Set environment variables (use SECRET_KEY above)"
echo "5. Deploy!"
```

---

## Custom Domain Setup

1. **Get Your Domain**
   - Purchase from Namecheap, GoDaddy, etc.

2. **Configure DNS**
   - Add CNAME record: `www` → `your-app.onrender.com`

3. **Update ALLOWED_HOSTS**
   - Add your domain: `yourdomain.com,www.yourdomain.com`

4. **Add Custom Domain in Render**
   - Go to Web Service → Settings → Custom Domain
   - Add your domain
   - SSL is automatic

---

## Success! 🎉

Your portfolio is now live! Share your URL and showcase your work.

**Your URL**: `https://your-app-name.onrender.com`

---

## Need Help?

- Check deployment logs in Render dashboard
- Verify all environment variables are set
- Test locally with production settings
- Review `DEPLOYMENT.md` for detailed instructions

---

**For a quick 5-minute deploy, see `QUICK_DEPLOY.md`**
