+-------------------+            +-------------------+            +-------------------+
|       User        | 1        * |   OutageReport    | *        1 |       Area        |
+-------------------+            +-------------------+            +-------------------+
| id (PK)           |            | id (PK)           |            | id (PK)           |
| username          |            | status (LIGHT/NO) |            | name (unique)     |
| email             |            | created_at        |            | state             |
| password          |            |                   |            | latitude          |
| location (opt)    |            | user_id (FK) ---->|            | longitude         |
| created_at        |            | area_id (FK) ---->|            |                   |
+-------------------+            +-------------------+            +-------------------+

+-------------------+
|   Notification    |
+-------------------+
| id (PK)           |
| message           |
| notif_type (enum) |
| status            |
| created_at        |
| user_id (FK) ---> |
+-------------------+

# 🔹 Explanation

* **User → OutageReport**:
  One user can submit many reports.

* **OutageReport → Area**:
  Each report belongs to a specific area (linked by GPS or manual search).

* **User → Notification**:
  Users can receive multiple notifications (future: push/email/SMS).