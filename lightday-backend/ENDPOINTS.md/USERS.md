### 1. **Auth (Users)**

* `POST /auth/register` → Register user.
    Request:
        {
            "username": "julius",
            "email": "julius@example.com",
            "password": "securePass123 "
        }
    Response:
        {
            "id": 1,
            "username": "julius",
            "email": "julius@example.com",
            "location": null,
            "created_at": "2025-09-13T10:15:00Z"
        }

* `POST /auth/login` → Login & get token.
    Request:
        {
            "email": "julius@example.com",
            "password": "securePass123"
        }
    Response:
        {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR...",
            "token_type": "Bearer",
            "user": {
                "id": 1,
                "username": "julius",
                "email": "julius@example.com"
            }
        }


* `GET /auth/me` → Get logged-in user profile.

### 4. **Notifications**

* `GET /notifications` → Get all notifications for logged-in user.
    Response:
        [
            {
                "id": 101,
                "message": "No Light reported in Yaba 10 mins ago.",
                "notif_type": "PUSH",
                "status": "SENT",
                "created_at": "2025-09-13T10:25:00Z"
            },
            {
                "id": 100,
                "message": "Power restored in Surulere.",
                "notif_type": "PUSH",
                "status": "SENT",
                "created_at": "2025-09-13T09:30:00Z"
            }
        ]

* `POST /notifications/send` → Trigger a new notification (admin or automated).

---

✅ This design ensures:

* A user can **see their area’s status** automatically (via `/outages/nearby`).
* A user can **search manually** for another area (via `/outages/area/:name`).
* Scales well for mobile + web.
