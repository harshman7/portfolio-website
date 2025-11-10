from django.core.management.base import BaseCommand
from portfolio.models import Profile, Education, Skill, WorkExperience, Project, Certification


class Command(BaseCommand):
    help = 'Load resume data into the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Loading resume data...'))

        # Create Profile
        profile, created = Profile.objects.get_or_create(
            full_name="Harshmanpreet Singh",
            defaults={
                'location': 'Edmonton, AB',
                'phone': '+1 7804460505',
                'email': 'harshman@ualberta.ca',
                'bio': 'Passionate software developer and data engineer with expertise in building scalable applications and data pipelines. Currently pursuing a Bachelor of Science in Computer Science at the University of Alberta.',
                'linkedin_url': '',  # Add your LinkedIn URL here
                'instagram_url': '',  # Add your Instagram URL here
                'github_url': '',  # Add your GitHub URL here
                'twitter_url': '',  # Add your Twitter URL here
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created profile'))
        else:
            self.stdout.write(self.style.WARNING('Profile already exists'))

        # Create Education
        education, created = Education.objects.get_or_create(
            institution="UNIVERSITY OF ALBERTA",
            defaults={
                'location': 'Edmonton, AB',
                'degree': 'Bachelor of Science',
                'major': 'Computer Science',
                'graduation_date': 'Expected June 2026',
                'gpa': 3.68,
                'description': 'Major in Computer Science. Cumulative GPA: 3.68/4.0',
                'order': 1
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created education'))
        else:
            self.stdout.write(self.style.WARNING('Education already exists'))

        # Create Skills
        skills_data = [
            # Frontend
            ('HTML/CSS', 'frontend', 5),
            ('JavaScript', 'frontend', 5),
            ('TypeScript', 'frontend', 4),
            ('React', 'frontend', 4),
            ('Angular', 'frontend', 3),
            ('Vue', 'frontend', 3),
            # Backend
            ('Python', 'backend', 5),
            ('Django', 'backend', 4),
            ('Flask', 'backend', 4),
            ('FastAPI', 'backend', 4),
            ('Node.js', 'backend', 4),
            ('Java', 'backend', 4),
            ('C#', 'backend', 3),
            ('ASP.NET Core', 'backend', 3),
            ('PHP', 'backend', 3),
            ('Laravel', 'backend', 3),
            ('Go', 'backend', 3),
            # Database
            ('SQL', 'database', 4),
            ('NoSQL', 'database', 4),
            # Cloud
            ('AWS', 'cloud', 4),
            ('Azure', 'cloud', 3),
            ('GCP', 'cloud', 3),
            # Tools
            ('Docker', 'tools', 4),
            ('Jira', 'tools', 4),
            ('Git', 'tools', 5),
        ]

        for name, category, proficiency in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=name,
                defaults={
                    'category': category,
                    'proficiency': proficiency,
                    'order': 0
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created skill: {name}'))

        # Create Work Experience
        # WFS Transport
        wfs_exp, created = WorkExperience.objects.get_or_create(
            company="WFS. Transport LTD.",
            position="Data Analyst Intern",
            defaults={
                'location': 'Milton, ON',
                'start_date': 'May 2023',
                'end_date': 'Jan 2024',
                'is_current': False,
                'description': 'As an Intern Data Analyst at WFS Transport ltd, a prominent trucking company, I played a pivotal role in leveraging data-driven insights to enhance operational efficiency and drive strategic decision-making. With a strong foundation in data analysis and a proficiency in Python and various statistical tools, I excelled in extracting actionable information from complex datasets and presenting it in a meaningful format. I learned alot from the company\'s founder Mr. Dave Walia, who has been operating the company since the last 17 years of its founding.',
                'achievements': [],
                'order': 2
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created WFS work experience'))

        # Disney Streaming
        disney_exp, created = WorkExperience.objects.get_or_create(
            company="Disney Streaming",
            position="Data Engineer",
            defaults={
                'location': 'New York, NY',
                'start_date': 'Sept 2024',
                'end_date': 'Feb 2025',
                'is_current': False,
                'description': 'Led end-to-end data migration efforts by coordinating with cross-functional teams to plan, execute, and validate seamless transitions across internal systems.',
                'achievements': [
                    'Ensured data integrity and consistency by developing automated ETL validation scripts and performing rigorous QA testing.',
                    'Diagnosed and resolved system performance issues post-migration, achieving a 30% improvement in data pipeline efficiency.',
                    'Created and maintained comprehensive technical documentation to support onboarding, scalability, and future migrations.',
                    'Contributed to scalability planning by profiling data workflows and recommending architectural optimizations.'
                ],
                'order': 1
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created Disney work experience'))

        # Create Projects
        # WHIMSY
        whimsy_project, created = Project.objects.get_or_create(
            title="WHIMSY - Social Media Application",
            defaults={
                'description': 'Developed a social media platform enabling users to share short-form "moods" and engage with others. Leveraged Firebase for authentication and data storage.',
                'tech_stack': 'Firebase, Java, XML, Kotlin, DALL•E',
                'project_date': 'Feb 2025',
                'features': [
                    'Follow/Following Feature: Built user follow relationships, allowing real-time updates on new posts.',
                    'AI-Driven Image Generation: Integrated DALL•E for mood-based image creation.',
                    'AI-Powered Responses: Added automatic mood explanations using the #generate-response hashtag.',
                    'Suggested Users: Implemented recommendation logic that suggests accounts to follow based on existing follow relationships.',
                    'User Interactions: Enabled user tagging, profile editing, and robust sign-in/sign-up flows for a seamless user experience.'
                ],
                'order': 2
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created WHIMSY project'))

        # Formula 1 Project
        f1_project, created = Project.objects.get_or_create(
            title="FORMULA 1 Race Outcome Predictor & Analytics Dashboard",
            defaults={
                'description': 'Developed an end-to-end predictive model to forecast Grand Prix wins using data from FastF1 API, incorporating driver performance, team dynamics, and track-specific features.',
                'tech_stack': 'Python, Pandas, Numpy, LightGBM, Scikit-Learn, SHAP, FastF1 API, Streamlit, Matplotlib, Seaborn',
                'project_date': 'Mar 2025',
                'features': [
                    'Engineered advanced features such as average lap times, teammate performance deltas, grid position impact, and normalized season progress metrics.',
                    'Implemented model interpretability using SHAP analysis to provide clear insights into key factors influencing race outcomes.',
                    'Addressed data imbalance and ensured robust predictions by calibrating the model with threshold tuning and class weighting in LightGBM.',
                    'Deployed an interactive Streamlit dashboard for real-time exploration, including visualizations of win probabilities, driver consistency across circuits, and team win rate breakdowns.',
                    'Improved data quality by integrating imputation techniques for missing team-level features, resulting in a model with enhanced accuracy and reliability for elite drivers.'
                ],
                'order': 1
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created Formula 1 project'))

        # Create Certifications
        certifications_data = [
            ('AWS Certified Solutions Architect - Associate', 'AWS', ''),
            ('Google Cloud Associate Cloud Engineer', 'Google Cloud', ''),
        ]

        for name, issuer, issue_date in certifications_data:
            cert, created = Certification.objects.get_or_create(
                name=name,
                defaults={
                    'issuer': issuer,
                    'issue_date': issue_date,
                    'order': 0
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created certification: {name}'))

        self.stdout.write(self.style.SUCCESS('Successfully loaded all resume data!'))

