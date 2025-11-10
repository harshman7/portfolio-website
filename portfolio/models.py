from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    """Personal profile information"""
    full_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True, help_text="Your LinkedIn profile URL")
    instagram_url = models.URLField(blank=True, help_text="Your Instagram profile URL")
    github_url = models.URLField(blank=True, help_text="Your GitHub profile URL")
    twitter_url = models.URLField(blank=True, help_text="Your Twitter/X profile URL")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Profile"


class Education(models.Model):
    """Education history"""
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    major = models.CharField(max_length=200, blank=True)
    graduation_date = models.CharField(max_length=50)
    gpa = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0.0), MaxValueValidator(4.0)],
        blank=True,
        null=True
    )
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Skill(models.Model):
    """Technical skills"""
    SKILL_CATEGORIES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('cloud', 'Cloud'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, default='other')
    proficiency = models.IntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Proficiency level from 1 to 5"
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    """Work experience"""
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    achievements = models.JSONField(default=list, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order']
        verbose_name_plural = "Work Experience"

    def __str__(self):
        return f"{self.position} at {self.company}"


class Project(models.Model):
    """Portfolio projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    features = models.JSONField(default=list, blank=True, help_text="List of project features")
    project_date = models.CharField(max_length=50, blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-order', '-created_at']

    def __str__(self):
        return self.title

    def get_tech_stack_list(self):
        """Return tech stack as a list"""
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]


class Certification(models.Model):
    """Certifications and training"""
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True)
    issue_date = models.CharField(max_length=50, blank=True)
    expiry_date = models.CharField(max_length=50, blank=True)
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order']
        verbose_name_plural = "Certifications"

    def __str__(self):
        return self.name
