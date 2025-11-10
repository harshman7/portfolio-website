# ✅ Deployment Checklist

## Pre-Deployment

- [ ] Code is committed to Git
- [ ] All dependencies in `requirements.txt`
- [ ] `DEBUG=False` for production
- [ ] `SECRET_KEY` is set via environment variable
- [ ] `ALLOWED_HOSTS` includes your domain
- [ ] Database is configured (PostgreSQL)
- [ ] Static files configuration is correct
- [ ] Media files configuration is correct

## Deployment Steps

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Ready for deployment"
git remote add origin YOUR_REPO_URL
git push -u origin main
```

### 2. Deploy Platform Setup

#### Render:
- [ ] Create PostgreSQL database
- [ ] Create Web Service
- [ ] Set environment variables
- [ ] Deploy

#### Railway:
- [ ] Create project
- [ ] Add PostgreSQL database
- [ ] Set environment variables
- [ ] Deploy

### 3. Environment Variables

Set these in your platform:
- [ ] `SECRET_KEY` (generate new one)
- [ ] `DEBUG=False`
- [ ] `ALLOWED_HOSTS=your-domain.com`
- [ ] `DATABASE_URL` (auto-set by platform)

### 4. Post-Deployment

- [ ] Run migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Load resume data: `python manage.py load_resume_data`
- [ ] Test website functionality
- [ ] Test admin panel
- [ ] Verify static files load
- [ ] Check mobile responsiveness
- [ ] Test scroll animations

## Generate Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Quick Test

```bash
# Test with production settings locally
DEBUG=False ALLOWED_HOSTS=localhost python manage.py runserver
```

---

**Ready to deploy! 🚀**

