# 🚀 Portfolio Website

A modern, interactive portfolio website built with Django, Tailwind CSS, and PostgreSQL.

## ✨ Features

- **Modern Design**: Dark theme with smooth animations
- **Responsive**: Works perfectly on all devices
- **Interactive**: Scroll-reveal animations, smooth transitions
- **Admin Panel**: Easy content management via Django admin
- **Dynamic Content**: Manage projects, skills, experience, and more

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone YOUR_REPO_URL
   cd portfolio-website
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Load resume data (optional)**
   ```bash
   python manage.py load_resume_data
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit**
   - Website: http://127.0.0.1:8000
   - Admin: http://127.0.0.1:8000/admin

## 📚 Documentation

All guides are in the `guides/` folder:

- **Quick Deploy**: `guides/QUICK_DEPLOY.md` - Deploy to Render in 5 minutes
- **Deployment Steps**: `guides/DEPLOY_STEPS.md` - Detailed deployment guide
- **Admin Guide**: `guides/ADMIN_GUIDE.md` - Managing content via admin panel
- **Project Summary**: `guides/PROJECT_SUMMARY.md` - Project overview

## 🌐 Deployment

This project is configured for deployment on **Render**.

### Quick Deploy to Render

1. Push your code to GitHub
2. Go to [Render.com](https://render.com)
3. Create a PostgreSQL database
4. Create a Web Service
5. Set environment variables
6. Deploy!

**For detailed instructions, see `guides/QUICK_DEPLOY.md`**

## 📁 Project Structure

```
portfolio-website/
├── portfolio/              # Main app
│   ├── models.py          # Database models
│   ├── views.py           # Views
│   ├── admin.py           # Admin configuration
│   └── management/        # Management commands
├── portfolio_project/     # Project settings
│   ├── settings.py        # Django settings
│   └── urls.py            # URL configuration
├── templates/             # HTML templates
├── static/                # Static files
├── guides/                # Documentation
├── render.yaml            # Render deployment config
└── requirements.txt       # Python dependencies
```

## 🛠️ Technology Stack

- **Backend**: Django 5.2.8
- **Database**: PostgreSQL (production) / SQLite (development)
- **Frontend**: Tailwind CSS (CDN)
- **Server**: Gunicorn
- **Static Files**: WhiteNoise

## 📝 Environment Variables

For production deployment, set these environment variables:

- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to `False` in production
- `ALLOWED_HOSTS` - Your domain
- `DATABASE_URL` - Database connection string (auto-set by Render)

## 🎨 Customization

- Edit content via Django admin panel at `/admin`
- Customize styles in `templates/portfolio/index.html`
- Update models in `portfolio/models.py`

## 📖 More Information

See the `guides/` folder for detailed documentation on:
- Deployment
- Admin panel usage
- Project features
- Configuration

## 📄 License

This project is open source and available for personal use.

## 🤝 Support

For deployment help, see `guides/DEPLOY_STEPS.md`

---

**Ready to deploy? Check out `guides/QUICK_DEPLOY.md`! 🚀**

