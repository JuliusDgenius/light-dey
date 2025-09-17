Product Requirements Document (PRD)
1. Overview
    • Product Name: Light Dey?
    • One-liner: A simple app that allows Nigerians to report and check electricity availability in their area.
    • Objective: Provide real-time visibility of power supply status per area to help residents make informed decisions.
2. Goals & Success Metrics
    • Primary Goal: Enable users to easily see if there’s light in their neighborhood.
    • Secondary Goals: Reduce misinformation about power status. Build a trusted community-driven reporting tool.
    • Success Metrics:
    • - At least 1,000 active users within 6 months.
    • - Users submit an average of 3+ reports per week.
    • - Accuracy >80% when cross-checked across multiple user reports.
3. Target Users
    • Primary: Nigerian households (students, families, workers).
    • Secondary: Small businesses (barbers, POS operators, welders) who rely on NEPA light.
    • User Needs: Quick check: 'Is there light in my area?'. Simple reporting: 'No light since morning'. Trust: Crowd-confirmed accuracy.
4. Features (MVP)
    • User Registration & Login (JWT-based)
    • Report Outage/Availability (tagged to feeder/area)
    • View Area Power Status (crowdsourced, latest reports visible)
    • Basic Admin Panel (moderation, flag suspicious reports)
5. Future Features (Post-MVP)
    • Push notifications: 'Light just returned in XYZ Feeder.'
    • Location-based auto-detection of feeder/area.
    • Leaderboard for most accurate reporters.
    • Integration with Disco APIs (if available).
6. Functional Requirements
    • Mobile & Web apps communicate with Django REST API.
    • Users must log in before submitting reports.
    • Reports stored in database with timestamps + user ID.
    • Only authenticated requests allowed for reporting.
    • Feeder/Area list preloaded (admin-managed).
7. Non-Functional Requirements
    • Performance: API responds < 1 second.
    • Scalability: Support 10k+ concurrent users.
    • Security: JWT authentication, password hashing, HTTPS.
    • Reliability: Reports stored even if network unstable (mobile offline sync).
8. Tech Stack
    • Backend: Django + Django REST Framework
    • Database: PostgreSQL
    • Frontend (Web): React.js
    • Mobile: React Native
    • Hosting: AWS / Azure / DigitalOcean
    • Auth: JWT (djangorestframework-simplejwt)
9. User Flow (MVP)
    • Registration/Login → User signs up or logs in.
    • Dashboard → User sees their area’s latest reports.
    • Submit Report → Select Feeder → Choose Status (Light/No Light) → Submit.
    • View Aggregated Data → See latest status updates, timestamps, and number of confirmations.
10. Risks & Mitigation
    • Fake reports → Allow upvotes/downvotes, moderation.
    • Low adoption → Community launch campaign, target students & SMEs.
    • Server downtime → Cloud hosting with monitoring.