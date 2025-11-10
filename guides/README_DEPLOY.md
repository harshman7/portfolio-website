# 🚀 Quick Deployment Guide - Render

## Deploy to Render (Easiest - Recommended)

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Portfolio website ready for deployment"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### Step 2: Deploy on Render

1. **Go to https://render.com** and sign up with GitHub

2. **Create PostgreSQL Database**
   - Click "New +" → "PostgreSQL"
   - Name: `portfolio-db`
   - Plan: Free
   - Create database
   - **Copy the Internal Database URL** (you'll need this)

3. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Settings:
     - **Name**: `portfolio-website` (or your preferred name)
     - **Environment**: `Python 3`
     - **Build Command**: 
       ```bash
       pip install -r requirements.txt && python manage.py collectstatic --noinput
       ```
     - **Start Command**: 
       ```bash
       gunicorn portfolio_project.wsgi:application
       ```

4. **Set Environment Variables**
   - Click "Environment" tab
   - Add these variables:
     ```
     SECRET_KEY=your-secret-key-here
     DEBUG=False
     ALLOWED_HOSTS=your-app-name.onrender.com
     DATABASE_URL=(paste the Internal Database URL from step 2)
     ```

   **Generate SECRET_KEY:**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait for build to complete (2-3 minutes)
   - Your site will be live at: `https://your-app-name.onrender.com`

### Step 3: Setup Database

After deployment, go to Render Shell or use Render's console:

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load resume data (optional)
python manage.py load_resume_data
```

**OR use Render's Shell:**
- Go to your Web Service → "Shell"
- Run the commands above

---

## Environment Variables

Create these in Render:

| Variable | Value | Description |
|----------|-------|-------------|
| `SECRET_KEY` | Generated key | Django secret key |
| `DEBUG` | `False` | Disable debug mode |
| `ALLOWED_HOSTS` | Your domain | Comma-separated domains |
| `DATABASE_URL` | Auto-set | Database connection (auto-set by platform when linked) |

---

## Post-Deployment Checklist

- [ ] Run migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Load resume data: `python manage.py load_resume_data`
- [ ] Test website: Visit your URL
- [ ] Test admin: Visit `/admin`
- [ ] Verify static files load correctly
- [ ] Check mobile responsiveness
- [ ] Test scroll animations

---

## Custom Domain

1. **Get your domain** (Namecheap, GoDaddy, etc.)

2. **Add DNS Record**
   - Type: CNAME
   - Name: `www`
   - Value: `your-app-name.onrender.com`

3. **Update ALLOWED_HOSTS**
   - Add your domain: `yourdomain.com,www.yourdomain.com`

4. **Add Custom Domain in Render**
   - Go to Web Service → Settings → Custom Domain
   - Add your domain
   - SSL will be automatically configured

---

## Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Database Connection Error
- Check `DATABASE_URL` is set correctly
- Verify PostgreSQL is running
- Check connection string format
- Verify database is linked to web service

### Build Fails
- Check Python version (3.11+)
- Verify all dependencies in `requirements.txt`
- Check build logs for errors

### 500 Error
- Check `DEBUG=False` is set
- Verify `ALLOWED_HOSTS` includes your domain
- Check application logs in platform dashboard

---

## Quick Commands

```bash
# Generate secret key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Test locally with production settings
DEBUG=False ALLOWED_HOSTS=localhost python manage.py runserver

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate
```

---

**Your portfolio is ready to deploy! 🎉**

For detailed instructions, see `DEPLOY_STEPS.md`
