# Django-rest-framework
### The Following commands to install Django framework in python (if you have python installed).
1. `pip install Django`
2. `pip install djangorestframework`

### open cmd in the location where you want to have the API project
## Installing django and djangorestframework
pip install Django
pip install djangorestframework

## to check django version
django.get_version() 

## To create a new Django Project of 'tango_with_django_project' name.
python c:\python27\scripts\django-admin.py startproject tango_with_django_project
django-admin startproject tango_with_django_project
			tango_with_django_project
					__init__.py :- indicates Python interpreter that the directory is a Python package.
					settings.py :- store all of your Django project’s settings.
					urls.py :- store URL patterns for your project.
					wsgi.py :-  run your development server and deploy your project to a production environment.
			manage.py


## To create the new application of "newApp" name.
python manage.py startapp newApp
django-admin startapp newapp
			tango_with_django_project
			manage.py
			newApp
					__init__.py:- indicates Python interpreter that the directory is a Python package.
					models.py:- store your application’s data models - where you specify the entities and relationships between data;
					tests.py:- store a series of functions to test your application’s code.
					views.py:- store a series of functions that take a clients’s requests and return responses.
					admin.py:- can register your models so that you can benefit from some Django machinery which creates an admin interface for you

## Django works on Model - view - Template (MVT) architectural design pattern 

## After creating a new application , you need to add it in settings.py
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newApp',
)

## Mapping URLs :- 
You need to create a new file "urls.py" under application directory which allow you to map URLs for your application (e.g. http://www.tangowithdjango.com/rango/) to specific views.

"""
python manage.py makemigrations 

output:- 
	Migrations for 'polls':
	  0001_initial.py:
		- Create model Question
		- Create model Choice
		- Add field question to choice

	By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
"""



"""
python manage.py migrate

migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app.
"""

## To create lightweight development server
python manage.py runserver 8080

python manage.py createsuperuser --email admin@example.com --username admin

