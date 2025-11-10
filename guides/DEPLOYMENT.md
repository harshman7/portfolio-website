# 🚀 Deployment Guide - Render

This guide will help you deploy your Django portfolio website to Render.

## 📋 Prerequisites

- Git repository (GitHub, GitLab, or Bitbucket)
- Python 3.11+
- Render account (free tier available)

## 🎯 Deploy to Render

### Step 1: Push to GitHub

1. **Initialize Git repository**
   ```bash
   git init
   git add .
   git commit -m "Portfolio website ready for deployment"
   ```

2. **Create GitHub repository**
   - Go to https://github.com/new
   - Name: `portfolio-website` (or your preferred name)
   - Create repository

3. **Push your code**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/portfolio-website.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Create Render Account

1. **Sign up for Render**
   - Go to https://render.com
   - Click "Get Started for Free"
   - Sign up with your GitHub account

### Step 3: Create PostgreSQL Database

1. **Create Database**
   - In Render Dashboard, click "New +" → "PostgreSQL"
   - Name: `portfolio-db`
   - Plan: **Free**
   - Region: Choose closest to you
   - Click "Create Database"
   - Wait for database to be created (1-2 minutes)

2. **Get Database URL**
   - Go to database → "Connections" tab
   - Copy the "Internal Database URL" (you'll need this)

### Step 4: Create Web Service

1. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub account (if not already)
   - Select your repository: `portfolio-website`
   - Click "Connect"

2. **Configure Web Service**
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

3. **Set Environment Variables**
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
     - Value: `(paste the Internal Database URL from Step 3)`

4. **Link Database (Optional)**
   - In Web Service settings, go to "Environment" tab
   - Click "Link Database" → Select your PostgreSQL database
   - This auto-sets `DATABASE_URL`

5. **Deploy**
   - Click "Create Web Service"
   - Wait for build to complete (3-5 minutes)
   - Your site will be live at: `https://portfolio-website.onrender.com`

### Step 5: Setup Database

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

## 🔧 Manual Deployment Steps

### 1. Generate Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 2. Set Environment Variables

In Render dashboard, set:

```env
SECRET_KEY=your-generated-secret-key
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
DATABASE_URL=postgresql://user:password@host:port/dbname
```

### 3. Install Dependencies

Render automatically runs:
```bash
pip install -r requirements.txt
```

### 4. Run Migrations

In Render Shell:
```bash
python manage.py migrate
```

### 5. Collect Static Files

Render automatically runs:
```bash
python manage.py collectstatic --noinput
```

### 6. Create Superuser

In Render Shell:
```bash
python manage.py createsuperuser
```

### 7. Load Resume Data (Optional)

In Render Shell:
```bash
python manage.py load_resume_data
```

---

## 🌐 Domain Configuration

### Custom Domain Setup

1. **Get Your Domain**
   - Purchase domain from Namecheap, GoDaddy, etc.

2. **Configure DNS**
   - Add CNAME record pointing to your Render URL
   - Example: `www` → `your-app.onrender.com`

3. **Update ALLOWED_HOSTS**
   - Add your domain to `ALLOWED_HOSTS` in Render
   - Example: `yourdomain.com,www.yourdomain.com`

4. **Add Custom Domain in Render**
   - Go to Web Service → Settings → Custom Domain
   - Add your domain
   - SSL will be automatically configured

---

## 📊 Database Setup

### PostgreSQL Setup

1. **Create Database**
   - Use Render's PostgreSQL service
   - Free tier is sufficient for most portfolios

2. **Get Connection String**
   - Format: `postgresql://user:password@host:port/dbname`
   - Set as `DATABASE_URL` environment variable
   - Or link database in Render (auto-sets `DATABASE_URL`)

3. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

4. **Load Data**
   ```bash
   python manage.py load_resume_data
   ```

---

## 🔒 Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Use strong `SECRET_KEY`
- [ ] Set `ALLOWED_HOSTS` correctly
- [ ] Enable HTTPS/SSL (automatic on Render)
- [ ] Use environment variables for secrets
- [ ] Enable security headers (auto-enabled when `DEBUG=False`)
- [ ] Use PostgreSQL in production
- [ ] Regular backups of database (Render provides automatic backups)

---

## 🐛 Troubleshooting

### Static Files Not Loading

1. **Check STATIC_ROOT**
   ```bash
   python manage.py collectstatic --noinput
   ```

2. **Verify WhiteNoise Middleware**
   - Should be in `MIDDLEWARE` after `SecurityMiddleware`

3. **Check Static Files URL**
   - Should be `/static/` in production

### Database Connection Issues

1. **Check DATABASE_URL**
   - Verify it's set in Render environment variables
   - Check database is linked to web service

2. **Verify PostgreSQL is running**
   - Check database status in Render dashboard
   - Verify database is not paused (free tier pauses after inactivity)

3. **Check environment variables**
   - Ensure all database vars are set
   - Verify `DATABASE_URL` format is correct

### Migration Issues

1. **Reset migrations (if needed)**
   ```bash
   python manage.py migrate --run-syncdb
   ```

2. **Check migration status**
   ```bash
   python manage.py showmigrations
   ```

### Build Failures

1. **Check Python version**
   - Should be 3.11+ (specified in `runtime.txt`)

2. **Verify requirements.txt**
   - All dependencies listed
   - Check build logs for missing packages

3. **Check build logs**
   - Look for error messages in Render dashboard
   - Verify build command is correct

### 500 Error

1. **Check DEBUG=False**
   - Verify `DEBUG` is set to `False`

2. **Verify ALLOWED_HOSTS**
   - Includes your Render domain
   - Check application logs in Render dashboard

3. **Check application logs**
   - View logs in Render dashboard
   - Look for error messages

### Database Paused (Free Tier)

Render free tier databases pause after 90 days of inactivity.

1. **Resume Database**
   - Go to database dashboard
   - Click "Resume" or "Activate"
   - Wait for database to resume

2. **Prevent Pausing**
   - Use database regularly
   - Or upgrade to paid plan

---

## 📝 Post-Deployment

### 1. Create Admin User

```bash
python manage.py createsuperuser
```

### 2. Load Resume Data

```bash
python manage.py load_resume_data
```

### 3. Verify Deployment

- Visit your site URL
- Check admin panel: `/admin`
- Verify all sections load correctly
- Test scroll animations
- Check mobile responsiveness

### 4. Set Up Monitoring

- Enable Render's monitoring
- Set up error tracking (optional)
- Configure database backups (automatic on Render)

---

## 🚀 Quick Start

```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Ready for deployment"
git remote add origin your-repo-url
git push -u origin main

# 2. Go to Render.com
# 3. Create PostgreSQL database
# 4. Create Web Service
# 5. Set environment variables
# 6. Deploy!

# 7. After deployment, run:
# - Migrations: python manage.py migrate
# - Create superuser: python manage.py createsuperuser
# - Load data: python manage.py load_resume_data
```

---

## 📞 Support

If you encounter issues:

1. Check deployment logs in Render dashboard
2. Verify environment variables are set
3. Test locally with production settings
4. Check Django documentation
5. Review Render documentation

---

## 🎯 Render Features

- **Free Tier**: Perfect for portfolios
- **Automatic SSL**: HTTPS enabled by default
- **Auto-Deploy**: Deploys on git push
- **Database Backups**: Automatic backups
- **Custom Domain**: Free custom domain support
- **Environment Variables**: Easy configuration
- **Shell Access**: Run commands easily

---

**Your portfolio is ready to deploy! 🎉**

For a quick 5-minute deploy, see `QUICK_DEPLOY.md`
