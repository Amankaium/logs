python -m venv logsvenv
call logsvenv\Scripts\activate
pip install django
django-admin startproject logs
cd logs
python manage.py runserver
python manage.py startapp core
python manage.py migrate
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate

git init
git add .
