# Django-rest-framework
#### The Following commands to install Django framework in python (if you have python installed).
   `pip install Django`<br>
   `pip install djangorestframework`

#### To check Django version
   `import django` <br>
   `django.get_version()`

#### Open cmd in the location where you want to have the REST API project
   `django-admin startproject project_name`<br>
    The following folder structure will be created under the folder project_name:
    
    project_name
    │   manage.py
    └───project_name
            settings.py
            urls.py
            wsgi.py
            __init__.py
    
    __init__.py : indicates Python interpreter that the directory is a Python package
    settings.py : store all of your Django project’s settings.
    urls.py     : store URL patterns for your project. 
    wsgi.py     : run your development server and deploy your project to a production environment.
    manage.py   : entry point for the REST API.
    

#### To create the new application of app_name.
   `cd project_name`<br>
   `django-admin startapp app_name`<br>
   Note: If the above command is not working then try `python manage.py startapp app_name` <br>
   The following folders/files will be added to the folder project_name:
    
    project_name
    │   manage.py
    │
    ├───app_name
    │   │   admin.py
    │   │   apps.py
    │   │   models.py
    │   │   tests.py
    │   │   views.py
    │   │   __init__.py
    │   │
    │   └───migrations
    │           __init__.py
    │
    └───project_name
            settings.py
            urls.py
            wsgi.py
            __init__.py
	    
	__init__.py: indicates Python interpreter that the directory is a Python package.<br>
	models.py  : store your application’s data models - where you specify the entities and relationships between data<br>
	tests.py   : store a series of functions to test your application’s code.<br>
	views.py   : store a series of functions that take a clients’s requests and return responses.<br>
	admin.py   : can register your models so that you can benefit from some Django machinery which creates an admin interface for you.

#### After creating a new application, you need to add `app_name` and `rest_framework` in settings.py
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app_name',
)
```

#### Create url.py inside the application
You need to create a new file "urls.py" under application directory which allow you to map URLs with the project

#### Apply migrations
    python manage.py makemigrations
	
 By running makemigrations, you’re asking Django that you have made changes to your models (in our case, when making new   application,creation of objects in model) and that you would like the changes to be stored as a migration.

    python manage.py migrate

 migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app."""

#### Locate manage.py file and run the following command there to run the server.
    python manage.py runserver 8080

#### Make urls.py in the app_name folder to have app level URLS.
The following will be now the folder structure

	project_name
	│   manage.py
	│
	├───app_name
	│   │   admin.py
	│   │   apps.py
	│   │   models.py
	│   │   tests.py
	│   │ 	urls.py
	│   │   views.py
	│   │   __init__.py
	│   │
	│   └───migrations
	│           __init__.py
	│
	└───project_name
		settings.py
		urls.py
		wsgi.py
		__init__.py
		
#### Add the app urls to main project by adding the following line in the urls.py at project level.

	path('project/',include('app_name.urls')),

Note: import include also. (from django.urls import path,include)<br>
urls.py will look like this now.

	from django.contrib import admin
	from django.urls import path,include
	from app_name.views import config

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('project/',include('app_name.urls')),
	]
	
#### add the views for the application.
    Please have a look at views.py file in app_name folder and the corresponding URLs in url.py	
