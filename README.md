# Sports Hub

Sports Hub is an educational sports information website for athletes, coaches, students, enthusiasts, and beginners. Visitors can open one public URL and browse sports without creating an account.

Tagline: **Everything Athletes Need in One Place**

This is not an official rulebook, medical service, or coaching certification. Official rules may vary by organisation, competition, and edition.

## Project layout

```
Sports website/
├── frontend/          Flutter Web app
├── backend/           Flask REST API
├── database/schema.sql
├── docker-compose.yml
├── render.yaml
└── README.md
```

## What is included

- Homepage with featured, popular, recent, and category cards
- Sport pages with the same section structure (overview through sources)
- Search across sports, rules, terms, equipment, techniques, and safety
- Category filters, rules hub, training hub, safety, about
- Browser bookmarks (local storage) — no account required
- Admin dashboard (JWT) to add/edit/delete sports, rules, equipment, techniques, sources, and categories
- PostgreSQL schema with separate tables and foreign keys
- Educational rule summaries that name the source organisation instead of inventing official text

## Requirements

- Python 3.11+
- PostgreSQL 14+ (or Docker)
- Flutter SDK (for the web frontend)

## 1. Database and API

```bash
docker compose up -d db
```

Copy environment variables (never commit real secrets):

```bash
copy backend\.env.example backend\.env
```

On macOS/Linux: `cp backend/.env.example backend/.env`

Set `SECRET_KEY`, `JWT_SECRET_KEY`, and `ADMIN_PASSWORD` to strong values.

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python seed.py
python app.py
```

API: `http://localhost:5000/api/health`

Seed creates 14 sports and an admin user from `ADMIN_EMAIL` / `ADMIN_PASSWORD`.

## 2. Flutter Web frontend

Install Flutter, then:

```bash
cd frontend
flutter pub get
flutter run -d chrome
```

Locally the app calls `http://localhost:5000`. After deployment it uses the same origin as the site unless you pass:

```bash
flutter build web --dart-define=API_BASE_URL=https://your-api.example.com
```

Place the built files in `frontend/build/web`. If that folder exists, Flask serves the UI and API on one public URL.

## 3. REST API (public)

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/sports` | List sports (`?category=&featured=true&popular=true`) |
| GET | `/api/sports/<id-or-slug>` | Sport detail |
| GET | `/api/categories` | Categories |
| GET | `/api/rules/<sport_id>` | Rules for a sport |
| GET | `/api/equipment/<sport_id>` | Equipment |
| GET | `/api/techniques/<sport_id>` | Techniques |
| GET | `/api/search?q=` | Full-site search |
| GET | `/api/safety` | General safety |
| GET | `/api/site/about` | About copy |

Admin (Bearer JWT, `role=admin` only):

- `POST/PUT/DELETE /api/admin/sports`
- `POST/PUT/DELETE /api/admin/rules`
- `POST/PUT/DELETE /api/admin/equipment`
- `POST/PUT/DELETE /api/admin/techniques`
- `POST/PUT/DELETE /api/admin/references`
- `POST/PUT/DELETE /api/admin/categories`

Auth: `POST /api/auth/login`, `POST /api/auth/register`, `GET /api/auth/me`

## 4. Admin

Open `/admin` in the Flutter app. Sign in with the seeded administrator. Regular visitors never receive an admin JWT.

When you change a rule, update **source organisation** and **rule edition/year**.

## 5. Security

- Passwords hashed with Werkzeug
- Admin routes require JWT + `admin` role
- SQLAlchemy parameterised queries
- CORS from `FRONTEND_ORIGIN`
- Secrets only in environment variables: `DATABASE_URL`, `SECRET_KEY`, `JWT_SECRET_KEY`, `ADMIN_PASSWORD`

## 6. Deploy for free (public link)

Yes, you can put Sports Hub on a **free public HTTPS URL**. Typical stack:

- **Render** free web service (the website). It sleeps after about 15 minutes of no traffic; the first visit after that can take ~30–60 seconds.
- **Neon** free PostgreSQL (does not expire after 30 days the way Render’s free database does).

You will need free accounts for **GitHub**, **Neon**, and **Render**.

### A. Put the project on GitHub

1. Create a GitHub account if you do not have one: https://github.com/signup
2. Create a new **public** repository, for example `sports-hub`.
3. From the project folder, push the code (do **not** push `backend/.env`).

### B. Create a free Postgres database (Neon)

1. Sign up at https://console.neon.tech
2. Create a project named `sports-hub`
3. Open **Dashboard → Connection string**
4. Copy the URI. It looks like `postgresql://...@...neon.tech/neondb?sslmode=require`

### C. Deploy the website (Render)

1. Sign up at https://render.com with GitHub
2. **New → Web Service** → connect the `sports-hub` repo
3. Settings:
   - **Root directory:** `backend`
   - **Runtime:** Python
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn -b 0.0.0.0:$PORT app:app`
   - **Instance type:** Free
4. Environment variables:

| Name | Value |
| --- | --- |
| `DATABASE_URL` | Neon connection string |
| `SECRET_KEY` | a long random string |
| `JWT_SECRET_KEY` | another long random string |
| `ADMIN_EMAIL` | an email you will use to sign in |
| `ADMIN_PASSWORD` | a strong password |
| `FRONTEND_ORIGIN` | `*` |
| `FLASK_ENV` | `production` |

5. Deploy. Your public link will look like `https://sports-hub-xxxx.onrender.com`

The first boot creates tables and loads the 14 sports if the database is empty. Open `/admin` on that URL to manage content.

Copy `frontend/build/web` into `backend/web` before you push if you want the full site (not only the API) on the same URL. `flutter build web --release` creates that folder.

## Accuracy policy

Rule modules are labelled educational / official summaries. They point to FIBA, FIVB, IFAB, BWF, ITF, ITTF, World Aquatics, World Athletics, WT, WBSC, UCI, and similar bodies. Always verify the current official document before officiating or competing.
