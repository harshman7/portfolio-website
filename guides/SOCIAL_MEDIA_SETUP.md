# 🔗 Social Media Setup Guide

## Quick Setup

### Step 1: Access Admin Panel
1. Start your server: `python manage.py runserver`
2. Go to: http://127.0.0.1:8000/admin/
3. Login with your superuser credentials

### Step 2: Add Social Media Links
1. Click on **"Profiles"** in the admin panel
2. Click on your profile to edit
3. Scroll to **"Social Media Links"** section
4. Add your URLs:
   - **LinkedIn URL**: `https://www.linkedin.com/in/your-profile/`
   - **Instagram URL**: `https://www.instagram.com/your-profile/`
   - **GitHub URL**: `https://github.com/your-username/`
   - **Twitter URL**: `https://twitter.com/your-username/`
5. Click **"Save"**

### Step 3: View Your Portfolio
1. Visit: http://127.0.0.1:8000/
2. Check the hero section for social media icons
3. Check the contact section
4. Check the footer

## 🎨 Social Media Icons Features

### LinkedIn
- Professional blue color on hover
- Icon: `fab fa-linkedin-in`
- Appears in: Hero, Contact, Footer

### Instagram
- Gradient pink/purple on hover
- Icon: `fab fa-instagram`
- Appears in: Hero, Contact, Footer

### GitHub
- Dark theme on hover
- Icon: `fab fa-github`
- Appears in: Hero, Contact, Footer

### Twitter
- Sky blue on hover
- Icon: `fab fa-twitter`
- Appears in: Hero, Contact, Footer

## ✨ Animation Effects

- **Hover Effect**: Icons scale and rotate
- **Color Transition**: Smooth color change
- **Ripple Effect**: Click animation
- **Smooth Transitions**: All animations are smooth

## 📍 Where Social Icons Appear

1. **Hero Section**: Large, animated icons below profile
2. **Contact Section**: Prominent display with email/phone
3. **Footer**: Clean, styled icons

## 🎯 Best Practices

1. **Use Full URLs**: Include `https://` in your URLs
2. **Test Links**: Make sure all links work
3. **Keep Updated**: Update links when they change
4. **Professional Links**: Use professional profiles only

## 🔧 Customization

### Change Icon Colors
Edit `templates/portfolio/index.html` and modify the CSS:
```css
.social-icon.linkedin:hover {
    background: #YOUR_COLOR;
}
```

### Add More Social Platforms
1. Add field to `Profile` model
2. Update admin panel
3. Add icon in template
4. Add CSS styling

## ❓ Troubleshooting

### Icons Not Showing
- Check if URLs are added in admin panel
- Verify URLs are valid
- Clear browser cache
- Check console for errors

### Icons Not Animating
- Check if JavaScript is enabled
- Verify CSS is loaded
- Check browser compatibility

### Links Not Working
- Verify URLs are correct
- Check if URLs include `https://`
- Test links in new tab
- Check if profiles are public

---

**Your social media links are now integrated with beautiful animations! 🎉**

