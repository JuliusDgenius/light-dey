lightdey-backend/
│
├── manage.py
├── requirements.txt           # Dependencies
├── .env                       # Environment variables
│
├── config/                    # Main project settings
│   ├── __init__.py
│   ├── settings.py            # Django settings (split: base, dev, prod if needed)
│   ├── urls.py                # Root URL routes
│   └── wsgi.py
│
├── apps/                      # All features live here (modular apps)
│   ├── users/                 # Authentication, profiles
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   │
│   ├── outages/               # Core feature: light reports
│   │   ├── models.py          # OutageReport model (status, area, timestamp, user)
│   │   ├── serializers.py
│   │   ├── views.py           # Endpoints (report outage, fetch status)
│   │   ├── urls.py
│   │   └── tests.py
│   │
│   └── notifications/         # Push/email/SMS notifications (future expansion)
│       ├── models.py
│       ├── services.py        # External integrations (e.g. Twilio, Firebase)
│       ├── tasks.py           # Celery tasks for async jobs
│       └── urls.py
│
├── scripts/                   # One-off scripts (e.g. seeding DB)
│
├── static/                    # Static files (if needed)
├── media/                     # User-uploaded files (if needed)
│
└── tests/                     # Centralized test suite (or keep inside each app)

