from django.contrib import admin
from .models import Profile, Education, Skill, WorkExperience, Project, Certification


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'location', 'phone', 'has_linkedin', 'has_instagram', 'updated_at']
    list_editable = ['email', 'location', 'phone']
    
    def has_linkedin(self, obj):
        return bool(obj.linkedin_url)
    has_linkedin.boolean = True
    has_linkedin.short_description = 'LinkedIn'
    
    def has_instagram(self, obj):
        return bool(obj.instagram_url)
    has_instagram.boolean = True
    has_instagram.short_description = 'Instagram'
    list_filter = ['updated_at', 'created_at']
    search_fields = ['full_name', 'email', 'location']
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'location', 'phone', 'email')
        }),
        ('Bio', {
            'fields': ('bio',)
        }),
        ('Profile Image', {
            'fields': ('profile_image',)
        }),
        ('Social Media Links', {
            'fields': ('linkedin_url', 'instagram_url', 'github_url', 'twitter_url'),
            'description': 'Add your social media profile URLs'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'major', 'graduation_date', 'gpa', 'order']
    list_editable = ['order']
    list_filter = ['graduation_date', 'gpa']
    search_fields = ['institution', 'degree', 'major']
    fieldsets = (
        ('Institution', {
            'fields': ('institution', 'location')
        }),
        ('Degree Information', {
            'fields': ('degree', 'major', 'graduation_date', 'gpa')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Display Order', {
            'fields': ('order',)
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_editable = ['category', 'proficiency', 'order']
    list_filter = ['category', 'proficiency']
    search_fields = ['name']
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'category', 'proficiency')
        }),
        ('Display Order', {
            'fields': ('order',)
        }),
    )


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'location', 'start_date', 'end_date', 'is_current', 'order']
    list_editable = ['order', 'is_current']
    list_filter = ['is_current', 'start_date', 'company']
    search_fields = ['company', 'position', 'location']
    fieldsets = (
        ('Company Information', {
            'fields': ('company', 'location')
        }),
        ('Position', {
            'fields': ('position', 'start_date', 'end_date', 'is_current')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Achievements', {
            'fields': ('achievements',),
            'description': 'Enter achievements as a JSON array, e.g., ["Achievement 1", "Achievement 2"]'
        }),
        ('Display Order', {
            'fields': ('order',)
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_date', 'order', 'created_at']
    list_editable = ['order']
    list_filter = ['project_date', 'created_at']
    search_fields = ['title', 'description', 'tech_stack']
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'project_date', 'description')
        }),
        ('Technical Details', {
            'fields': ('tech_stack', 'features'),
            'description': 'Tech stack: Comma-separated list. Features: JSON array, e.g., ["Feature 1", "Feature 2"]'
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Display Order', {
            'fields': ('order',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'issue_date', 'expiry_date', 'order']
    list_editable = ['order']
    list_filter = ['issuer', 'issue_date']
    search_fields = ['name', 'issuer']
    fieldsets = (
        ('Certification Information', {
            'fields': ('name', 'issuer')
        }),
        ('Dates', {
            'fields': ('issue_date', 'expiry_date')
        }),
        ('Credentials', {
            'fields': ('credential_id', 'credential_url')
        }),
        ('Display Order', {
            'fields': ('order',)
        }),
    )


# Customize admin site header and title
admin.site.site_header = "Portfolio Administration"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"
