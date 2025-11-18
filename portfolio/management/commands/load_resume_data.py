from django.core.management.base import BaseCommand
from portfolio.models import Profile, Education, Skill, WorkExperience, Project, Certification


class Command(BaseCommand):
    help = 'Load resume data into the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Loading resume data...'))

        # Create/Update Profile
        profile, created = Profile.objects.get_or_create(
            full_name="Harshmanpreet Singh",
            defaults={
                'location': 'Edmonton, AB',
                'phone': '780-446-0505',
                'email': 'harshman@ualberta.ca',
                'bio': 'Data Engineer and Software Developer with expertise in building scalable data pipelines, ETL systems, and full-stack applications. Currently pursuing a Bachelor of Science in Computing Science at the University of Alberta.',
                'linkedin_url': 'https://www.linkedin.com/in/harshmanpreet',
                'instagram_url': '',
                'github_url': 'https://github.com/harshman7',
                'twitter_url': '',
            }
        )
        if not created:
            # Update existing profile
            profile.location = 'Edmonton, AB'
            profile.phone = '780-446-0505'
            profile.email = 'harshman@ualberta.ca'
            profile.bio = 'Data Engineer and Software Developer with expertise in building scalable data pipelines, ETL systems, and full-stack applications. Currently pursuing a Bachelor of Science in Computing Science at the University of Alberta.'
            profile.linkedin_url = 'https://www.linkedin.com/in/harshmanpreet'
            profile.github_url = 'https://github.com/harshman7'
            profile.save()
            self.stdout.write(self.style.SUCCESS('Updated profile'))
        else:
            self.stdout.write(self.style.SUCCESS('Created profile'))

        # Create/Update Education
        education, created = Education.objects.get_or_create(
            institution="University of Alberta",
            defaults={
                'location': 'Edmonton, AB',
                'degree': 'Bachelor of Science in Computing Science',
                'major': 'Computing Science',
                'graduation_date': 'Class of 2026',
                'gpa': 3.68,
                'description': 'Bachelor of Science in Computing Science. Cumulative GPA: 3.68',
                'order': 1
            }
        )
        if not created:
            education.degree = 'Bachelor of Science in Computing Science'
            education.major = 'Computing Science'
            education.graduation_date = 'Class of 2026'
            education.gpa = 3.68
            education.description = 'Bachelor of Science in Computing Science. Cumulative GPA: 3.68'
            education.save()
            self.stdout.write(self.style.SUCCESS('Updated education'))
        else:
            self.stdout.write(self.style.SUCCESS('Created education'))

        # Create Skills
        skills_data = [
            # Frontend
            ('HTML', 'frontend', 5),
            ('Tailwind CSS', 'frontend', 4),
            ('JavaScript/TypeScript', 'frontend', 5),
            ('React', 'frontend', 4),
            # Backend
            ('Python', 'backend', 5),
            ('Django', 'backend', 4),
            ('FastAPI', 'backend', 5),
            ('Java', 'backend', 4),
            ('Java/Kotlin (Android)', 'backend', 4),
            ('C', 'backend', 3),
            ('C++', 'backend', 3),
            # Database
            ('SQL (PostgreSQL, SQLite)', 'database', 5),
            # Cloud
            ('AWS', 'cloud', 4),
            # Tools
            ('Docker', 'tools', 4),
            ('Git', 'tools', 5),
            ('Jira', 'tools', 4),
            ('LangChain', 'tools', 4),
            ('LangGraph', 'tools', 4),
            ('Langsmith', 'tools', 3),
            ('Cursor', 'tools', 4),
            # Machine Learning
            ('Machine Learning (ANN, CNN)', 'other', 4),
            ('Pandas', 'other', 5),
            ('NumPy', 'other', 5),
            ('scikit-learn', 'other', 4),
            ('LightGBM', 'other', 4),
            ('RAG (Retrieval-Augmented Generation)', 'other', 4),
            ('Streamlit', 'other', 4),
            ('Firebase', 'other', 4),
            ('Celery', 'other', 3),
            ('Linux', 'other', 4),
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

        # Create/Update Work Experience
        # Disney Streaming (Most Recent)
        disney_exp, created = WorkExperience.objects.get_or_create(
            company="Disney Streaming",
            position="Data Engineer",
            defaults={
                'location': 'New York City, New York',
                'start_date': 'September 2024',
                'end_date': 'May 2025',
                'is_current': False,
                'description': 'Led planning, execution, and validation of cross-system data migrations, partnering with product, infrastructure, and analytics teams to minimize downtime and defects.',
                'achievements': [
                    'Built automated ETL validation suites (schema checks, row-level reconciliations, data-quality alerts) to ensure data integrity and consistency across legacy and target platforms.',
                    'Optimized batch and streaming data pipelines post-migration (partitioning, indexing, concurrency), improving end-to-end performance by ~30% and stabilizing SLAs.',
                    'Authored and maintained migration runbooks, technical documentation, and architecture diagrams to speed onboarding and de-risk future migration waves.'
                ],
                'order': 1
            }
        )
        if not created:
            disney_exp.location = 'New York City, New York'
            disney_exp.start_date = 'September 2024'
            disney_exp.end_date = 'May 2025'
            disney_exp.description = 'Led planning, execution, and validation of cross-system data migrations, partnering with product, infrastructure, and analytics teams to minimize downtime and defects.'
            disney_exp.achievements = [
                'Built automated ETL validation suites (schema checks, row-level reconciliations, data-quality alerts) to ensure data integrity and consistency across legacy and target platforms.',
                'Optimized batch and streaming data pipelines post-migration (partitioning, indexing, concurrency), improving end-to-end performance by ~30% and stabilizing SLAs.',
                'Authored and maintained migration runbooks, technical documentation, and architecture diagrams to speed onboarding and de-risk future migration waves.'
            ]
            disney_exp.save()
            self.stdout.write(self.style.SUCCESS('Updated Disney work experience'))
        else:
            self.stdout.write(self.style.SUCCESS('Created Disney work experience'))

        # AccelerEd
        accelered_exp, created = WorkExperience.objects.get_or_create(
            company="AccelerEd (via SKKY Analytics & Consulting Inc.)",
            position="Data Intern",
            defaults={
                'location': 'Adelphi, Maryland',
                'start_date': 'May 2025',
                'end_date': 'September 2025',
                'is_current': False,
                'description': 'Supported data operations for higher-education systems by extracting, cleaning, and reconciling student and administrative records across PeopleSoft, OnBase, and internal tools.',
                'achievements': [
                    'Built ad-hoc reports for enrollment and finance stakeholders, performed routine data quality checks (duplicates, missing fields, cross-system mismatches), and documented data flows and issues to improve onboarding and handover as the product transitioned back into UMGC Ventures.',
                    'Used SQL and spreadsheet-based analysis to answer stakeholder data questions, streamline recurring reporting tasks, and surface anomalies needing business review.',
                    'Collaborated with product and operations teams to translate business questions into repeatable queries and reporting templates, improving clarity and consistency of data requests.'
                ],
                'order': 2
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created AccelerEd work experience'))

        # WFS Transport
        wfs_exp, created = WorkExperience.objects.get_or_create(
            company="WFS. Transport Ltd.",
            position="Data Intern",
            defaults={
                'location': 'Milton, Ontario',
                'start_date': 'May 2023',
                'end_date': 'January 2024',
                'is_current': False,
                'description': 'Analyzed large transportation and logistics datasets using Python and statistical tools to generate actionable insights for operations.',
                'achievements': [
                    'Developed and maintained reports/dashboards to track key KPIs (route efficiency, load utilization, on-time performance) for leadership.',
                    'Partnered closely with the company\'s founder, contributing data-driven input to strategic decisions in a trucking business operating for 17+ years.',
                    'Streamlined recurring operations reporting by standardizing data pulls and templates, reducing manual effort for weekly performance reviews.'
                ],
                'order': 3
            }
        )
        if not created:
            wfs_exp.position = 'Data Intern'
            wfs_exp.location = 'Milton, Ontario'
            wfs_exp.start_date = 'May 2023'
            wfs_exp.end_date = 'January 2024'
            wfs_exp.description = 'Analyzed large transportation and logistics datasets using Python and statistical tools to generate actionable insights for operations.'
            wfs_exp.achievements = [
                'Developed and maintained reports/dashboards to track key KPIs (route efficiency, load utilization, on-time performance) for leadership.',
                'Partnered closely with the company\'s founder, contributing data-driven input to strategic decisions in a trucking business operating for 17+ years.',
                'Streamlined recurring operations reporting by standardizing data pulls and templates, reducing manual effort for weekly performance reviews.'
            ]
            wfs_exp.order = 3
            wfs_exp.save()
            self.stdout.write(self.style.SUCCESS('Updated WFS work experience'))
        else:
            self.stdout.write(self.style.SUCCESS('Created WFS work experience'))

        # Create/Update Projects
        # DocSage (Most Recent)
        docsage_project, created = Project.objects.get_or_create(
            title="DocSage (Intelligent Document Processing & Analytics)",
            defaults={
                'description': 'Built an end-to-end "insight agent" that ingests PDF documents, performs OCR, extracts structured fields, and stores them in a relational database.',
                'tech_stack': 'Python, FastAPI, Streamlit, PostgreSQL, FAISS, Ollama, Docker',
                'project_date': '2025',
                'features': [
                    'Implemented a local RAG pipeline with sentence-transformer embeddings and FAISS so the agent can ground its answers in document content.',
                    'Designed a tool-using LLM agent (SQL, metrics, and RAG tools) that can answer questions like "which invoices are overdue and how has that changed month-over-month?" using real database queries.',
                    'Exposed the system via FastAPI and a Streamlit UI, using Docker + docker-compose with PostgreSQL to mirror an AWS-style architecture (Textract + RDS + OpenSearch + Bedrock) at zero cost.'
                ],
                'order': 1
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created DocSage project'))

        # Whimsy
        whimsy_project, created = Project.objects.get_or_create(
            title="Whimsy (Social Media Application)",
            defaults={
                'description': 'Built a full-stack social platform for sharing short-form "moods," using Firebase for authentication, data storage, and robust sign-in/sign-up flows.',
                'tech_stack': 'Firebase, Java, XML, Kotlin, DALL-E',
                'project_date': '2025',
                'features': [
                    'Implemented social features including follow relationships, real-time feeds, user tagging, profile editing, and recommendation logic to suggest accounts to follow.',
                    'Integrated AI features such as DALL·E-based mood image generation and automatic mood explanations triggered via the `#generate-response` hashtag.'
                ],
                'order': 2
            }
        )
        if not created:
            whimsy_project.title = 'Whimsy (Social Media Application)'
            whimsy_project.description = 'Built a full-stack social platform for sharing short-form "moods," using Firebase for authentication, data storage, and robust sign-in/sign-up flows.'
            whimsy_project.tech_stack = 'Firebase, Java, XML, Kotlin, DALL-E'
            whimsy_project.features = [
                'Implemented social features including follow relationships, real-time feeds, user tagging, profile editing, and recommendation logic to suggest accounts to follow.',
                'Integrated AI features such as DALL·E-based mood image generation and automatic mood explanations triggered via the `#generate-response` hashtag.'
            ]
            whimsy_project.save()
            self.stdout.write(self.style.SUCCESS('Updated Whimsy project'))
        else:
            self.stdout.write(self.style.SUCCESS('Created Whimsy project'))

        # GridSense (Formula 1) - Handle old project name migration
        old_f1_project = Project.objects.filter(title__icontains="FORMULA 1").first()
        if old_f1_project:
            old_f1_project.title = 'GridSense (Formula One Outcome Predictor)'
            old_f1_project.description = 'Built an end-to-end LightGBM model using FastF1 race data to predict Grand Prix winners, incorporating driver performance, team dynamics, and track-specific features (e.g., grid position impact, teammate deltas, normalized season progress).'
            old_f1_project.tech_stack = 'Python, NumPy, Pandas, LightGBM, scikit-learn, SHAP, FastF1 API, Streamlit, Matplotlib, Seaborn'
            old_f1_project.features = [
                'Improved model robustness and accuracy by engineering advanced features, imputing missing team-level data, and addressing class imbalance via threshold tuning and class weighting, with interpretability provided through SHAP analysis.',
                'Deployed an interactive Streamlit analytics dashboard to visualize win probabilities, driver consistency by circuit, and team win-rate breakdowns for real-time exploration.'
            ]
            old_f1_project.order = 3
            old_f1_project.save()
            self.stdout.write(self.style.SUCCESS('Updated GridSense project (migrated from old Formula 1 project)'))
        else:
            gridsense_project, created = Project.objects.get_or_create(
                title="GridSense (Formula One Outcome Predictor)",
                defaults={
                    'description': 'Built an end-to-end LightGBM model using FastF1 race data to predict Grand Prix winners, incorporating driver performance, team dynamics, and track-specific features (e.g., grid position impact, teammate deltas, normalized season progress).',
                    'tech_stack': 'Python, NumPy, Pandas, LightGBM, scikit-learn, SHAP, FastF1 API, Streamlit, Matplotlib, Seaborn',
                    'project_date': '2025',
                    'features': [
                        'Improved model robustness and accuracy by engineering advanced features, imputing missing team-level data, and addressing class imbalance via threshold tuning and class weighting, with interpretability provided through SHAP analysis.',
                        'Deployed an interactive Streamlit analytics dashboard to visualize win probabilities, driver consistency by circuit, and team win-rate breakdowns for real-time exploration.'
                    ],
                    'order': 3
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS('Created GridSense project'))
            else:
                gridsense_project.description = 'Built an end-to-end LightGBM model using FastF1 race data to predict Grand Prix winners, incorporating driver performance, team dynamics, and track-specific features (e.g., grid position impact, teammate deltas, normalized season progress).'
                gridsense_project.tech_stack = 'Python, NumPy, Pandas, LightGBM, scikit-learn, SHAP, FastF1 API, Streamlit, Matplotlib, Seaborn'
                gridsense_project.features = [
                    'Improved model robustness and accuracy by engineering advanced features, imputing missing team-level data, and addressing class imbalance via threshold tuning and class weighting, with interpretability provided through SHAP analysis.',
                    'Deployed an interactive Streamlit analytics dashboard to visualize win probabilities, driver consistency by circuit, and team win-rate breakdowns for real-time exploration.'
                ]
                gridsense_project.save()
                self.stdout.write(self.style.SUCCESS('Updated GridSense project'))

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

