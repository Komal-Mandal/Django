# Django

python -m venv env  # Create virtual environment

env\Scripts\activate  # Activate (Windows) 

source env/bin/activate (Mac/Linux)

mkdir ch1 && cd ch1  # Create and navigate to 'ch1' folder

pip install django  # Install Django

django-admin startproject ch1 .  # Create Django project in current folder

python manage.py startapp app1  # Create Django app 'app1'

python manage.py runserver  # Start development server


manage.py makemigration

python manage.py makemigrations

python manage.py sqlmigrate student 0001

python manage.py migrate