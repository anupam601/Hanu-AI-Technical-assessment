# 🗺️ Map API Project (Django + REST Framework)

## 📌 Project Overview
This Django-based project provides:
- A REST API to serve location data in **GeoJSON** format
- Basic **statistics** like total locations and most common category
- A **Django admin panel** to manage location entries
- A **simple HTML + JavaScript frontend** to display the API data

---

## 🚀 How to Run the Project

### 1. Clone or Download
Place the project in a folder on your system. Example:
D:\map_api_project

r
Copy code

### 2. Open Terminal in Project Folder
Navigate into the folder that contains `manage.py`.

### 3. Create a Virtual Environment
```bash
python -m venv env
env\Scripts\activate  # For Windows
4. Install Required Packages
bash
Copy code
pip install django djangorestframework django-cors-headers
5. Configure Django
Make sure the following are added in map_api_project/settings.py:

In INSTALLED_APPS:
python
Copy code
'rest_framework',
'corsheaders',
'locations',
In MIDDLEWARE:
Add at the top:

python
Copy code
'corsheaders.middleware.CorsMiddleware',
At the bottom:
python
Copy code
CORS_ALLOW_ALL_ORIGINS = True
6. Migrate the Database
bash
Copy code
python manage.py makemigrations
python manage.py migrate
7. Create Superuser
bash
Copy code
python manage.py createsuperuser
8. Run the Server
bash
Copy code
python manage.py runserver
Visit:

http://127.0.0.1:8000/admin/ – Admin panel to add locations

http://127.0.0.1:8000/api/geojson/ – Location data in GeoJSON format

http://127.0.0.1:8000/api/stats/ – Total and most common category

📄 Frontend
Open the index.html file in your browser. It will:

Fetch and show location stats

List all locations by name and category
