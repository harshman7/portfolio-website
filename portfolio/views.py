from django.shortcuts import render
from .models import Profile, Education, Skill, WorkExperience, Project, Certification


def index(request):
    """Main portfolio page"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    education = Education.objects.all()
    skills = Skill.objects.all()
    work_experience = WorkExperience.objects.all()
    projects = Project.objects.all()
    certifications = Certification.objects.all()
    
    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    context = {
        'profile': profile,
        'education': education,
        'skills_by_category': skills_by_category,
        'work_experience': work_experience,
        'projects': projects,
        'certifications': certifications,
    }
    
    return render(request, 'portfolio/index.html', context)
