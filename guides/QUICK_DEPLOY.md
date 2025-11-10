# ⚡ Quick Deploy Guide

## 🚀 Deploy in 5 Minutes (Render)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Portfolio ready for deployment"
git remote add origin YOUR_REPO_URL
git push -u origin main
```

### 2. Deploy on Render

1. **Go to https://render.com** → Sign up with GitHub

2. **Create PostgreSQL**
   - New + → PostgreSQL → Free → Create
   - Copy "Internal Database URL"

3. **Create Web Service**
   - New + → Web Service → Connect repo
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn portfolio_project.wsgi:application`

4. **Set Environment Variables**
   ```
   SECRET_KEY=(generate with command below)
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.onrender.com
   DATABASE_URL=(paste Internal Database URL)
   ```

5. **Generate Secret Key**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

6. **Deploy** → Wait 3-5 minutes → Done! 🎉

### 3. Setup Database
```bash
# In Render Shell:
python manage.py migrate
python manage.py createsuperuser
python manage.py load_resume_data
```

### 4. Visit Your Site
**https://your-app-name.onrender.com**

---

## 🎯 That's It!

Your portfolio is live! For detailed instructions, see `guides/DEPLOY_STEPS.md`

---

## 🔧 Quick Commands

```bash
# Generate secret key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Test locally
DEBUG=False ALLOWED_HOSTS=localhost python manage.py runserver

# Collect static files
python manage.py collectstatic --noinput
```

---

**Need help? Check `guides/DEPLOY_STEPS.md` for detailed instructions!**

