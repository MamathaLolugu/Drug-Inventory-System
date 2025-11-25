# Smart Drug Tracking System

**Overview:**  
A Django-based web application to **manage drug inventory, track drug movements, and verify drug authenticity via QR codes** with a user-friendly dashboard. It ensures transparency, reduces errors, and prevents misuse in pharmaceutical supply chains.

**Problem Statement:**  
Manual drug inventory management often leads to errors, misuse, and lack of transparency. This system provides a smart solution for managing inventories, tracking movement history, and verifying drugs via QR codes.

**Features:**  
- Add, update, and manage drug inventory  
- Track the movement history of drugs  
- Scan QR codes to verify authenticity  
- User-friendly dashboard for real-time insights

**Project Structure / Uploaded Files:**  
- `drugtrack/` → Project configuration (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`, `__init__.py`)  
- `inventory/` → Main app with models, views, URLs, admin, and static files  
- `templates/inventory/` → HTML templates for UI  
- `static/` → CSS and frontend assets  
- `migrations/` → Database migration files  
- `manage.py` → Django command-line utility  
- `db.sqlite3` → SQLite database  

**Installation & Setup:**  
```bash
pip install django
django-admin startproject drugtrack
python manage.py startapp inventory
python manage.py makemigrations
python manage.py migrate
```
Purpose:
Designed to help pharmacies and healthcare providers efficiently manage inventories, track drug movements, and verify drug authenticity, reducing errors and improving transparency.

👩‍💻 Developer Information

Developer: Mamatha Lolugu

GitHub:https://github.com/MamathaLolugu

Linkedin:https://www.linkedin.com/in/mamathalolugu
