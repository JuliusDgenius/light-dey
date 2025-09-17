### 2. **Outages**

* `POST /outages/report`

  * Body: `{ areaId, status }` OR `{ latitude, longitude, status }`.
  * Creates a new report.

  {
    "areaId": 3,
    "status": "NO_LIGHT"
  }
  Response:
    {
      "id": 15,
      "user": {
        "id": 1,
        "username": "julius"
      },
      "area": {
        "id": 3,
        "name": "Yaba",
        "state": "Lagos"
      },
      "status": "NO_LIGHT",
      "created_at": "2025-09-13T10:20:00Z"
    }

* `GET /outages/area/:name`

  * Returns latest reports for a given area (manual search).
    Response:
      {
        "area": {
        "id": 3,
        "name": "Yaba",
        "state": "Lagos"
        },
        "reports": [
        {
          "id": 15,
          "status": "NO_LIGHT",
          "reported_by": "julius",
          "created_at": "2025-09-13T10:20:00Z"
        },
        {
          "id": 14,
          "status": "LIGHT",
          "reported_by": "amina",
          "created_at": "2025-09-13T09:45:00Z"
        }
        ]
      }

* `GET /outages/nearby?lat=6.5244&lng=3.3792&radius=5`

  * Returns reports near user’s current location.
    Response:
      {
        "user_location": {
          "latitude": 6.5244,
          "longitude": 3.3792
        },
        "nearby_reports": [
          {
            "id": 15,
            "area": "Yaba",
            "status": "NO_LIGHT",
            "reported_by": "julius",
            "created_at": "2025-09-13T10:20:00Z"
          },
          {
            "id": 13,
            "area": "Surulere",
            "status": "LIGHT",
            "reported_by": "chioma",
            "created_at": "2025-09-13T09:10:00Z"
          }
        ]
      }

* `GET /outages/latest`

  * Returns the **most recent outage reports globally** (like a feed).

---