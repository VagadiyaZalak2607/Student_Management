
# StudentCRUD Project

## Overview
This is a simple Django CRUD application for managing student records.
It includes:
- A `Student` model with fields: `name`, `email`, `course`, `admission_date`, and `fees`
- Admin panel registration for managing student data
- Pre-generated migrations (you can directly run `migrate`)

---

## Setup Instructions

1. **Extract the ZIP**
   ```bash
   unzip StudentCRUD_Project_ready.zip
   cd StudentCRUD_Project_fixed
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate     # On Windows
   # or source venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies**
   ```bash
   pip install django
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```

Visit http://127.0.0.1:8000/admin to access the admin dashboard.

---

✅ Project prepared and verified to be migration-ready.
