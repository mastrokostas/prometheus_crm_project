# Prometheus CRM

A property management CRM built with Django, designed to manage the full lifecycle of construction rental properties — from ownership and construction tracking to tenant agreements and monthly payment records.

Built from scratch as a personal proof-of-concept project. No tutorials were followed for the domain logic — the data model and workflows reflect real-world property management needs.

---

## What it does

The system is organized around 8 Django apps:

- **Properties** — tracks each apartment unit: address, floor, surface area, construction status, furnishing status, utilisation type (long-term/short-term/managed), utility account credentials, building management details, and rental guarantee info
- **Landlords** — manages property owners with full legal and contact details, cooperation type, and law firm assignment
- **Tenants** — stores tenant records including tax ID, ID document, blacklist status, and legal action flags
- **LT Rentals** — handles long-term rental agreements, linking a property to one or two tenants, tracking rent amount, contract dates, months paid/remaining/owed, and expiry status
- **Monthly Payments** — records individual rent payments per agreement (amount, date, method, month covered)
- **Collaborators** — manages third-party companies: electricity providers, natural gas providers, law firms, subcontractors, furniture providers, and building management companies
- **Search** — cross-model search functionality
- **Users** — authentication with role-based access control via custom decorators

---

## Tech stack

- Python 3.12
- Django 5.0.6
- SQLite (development database)
- Bootstrap (frontend)
- python-decouple (environment variable management)

---

## How to run locally

**1. Clone the repo**
```bash
git clone https://github.com/mastrokostas/prometheus_crm_project.git
cd prometheus_crm_project
```

**2. Create and activate a virtual environment**
```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create a `.env` file in the project root**
```
SECRET_KEY=your-secret-key-here
```

You can generate a new Django secret key with:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**5. Run migrations**
```bash
python manage.py migrate
```

**6. Create a superuser**
```bash
python manage.py createsuperuser
```

**7. Start the development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## Project status

Proof of concept. The core data models and CRUD flows are functional. Known limitations:

- No test coverage
- SQLite only (not production-ready)
- `DEBUG = True` (not configured for deployment)
- Some views and forms are incomplete
- Role-based access control is partially implemented

---

## Author

Konstantinos Koletsis