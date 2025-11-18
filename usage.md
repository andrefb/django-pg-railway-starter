python -m venv env

env\Scripts\activate

pip install django

pip install -r requirements.txt

python manage.py runserver


django-admin startproject mysite

python manage.py runserver


## Configure Database, Static Files & Dependencies

python -m pip install gunicorn whitenoise psycopg[binary,pool]


## open mysite.settings.py and replace the sqlite database with

import os
from pathlib import Path


´´´
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Set default values for the environment variables if they’re not already set
os.environ.setdefault("PGDATABASE", "liftoff_dev")
os.environ.setdefault("PGUSER", "username")
os.environ.setdefault("PGPASSWORD", "")
os.environ.setdefault("PGHOST", "localhost")
os.environ.setdefault("PGPORT", "5432")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["PGDATABASE"],
        'USER': os.environ["PGUSER"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
    }
}

´´´

## Configure statifiles settings

´´´
STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
´´´


## Add the WhiteNoise middleware in the MIDDLEWARE section, just below the security middleware:

´´´
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

´´´

## update ALLOWED_HOSTS

ALLOWED_HOSTS = ["*"]


## Create a static folder:
Inside your mysite directory, create a static folder where all static assets will reside.


# make requirements.txt

pip freeze > requirements.txt



## get ready to deploy

railway init
railway up

# add database
railway add.


Add a Database Service:
Run railway add.

Select PostgreSQL by pressing space and hit Enter to add it to your project.
A database service will be added to your Railway project.



Configure Environment Variables:
Go to your app service Variables section and add the following:
PGDATABASE: Set the value to ${{Postgres.PGDATABASE}} (this references the Postgres database name). Learn more about referencing service variables.
PGUSER: Set the value to ${{Postgres.PGUSER}}
PGPASSWORD: Set the value to ${{Postgres.PGPASSWORD}}
PGHOST: Set the value to ${{Postgres.PGHOST}}
PGPORT: Set the value to ${{Postgres.PGPORT}}
Use the Raw Editor to add any other required environment variables in one go.
Redeploy the App Service:
Click Deploy on the app service on the Railway dashboard to apply your changes.


Set Up a Public URL:
Navigate to the Networking section under the Settings tab of your new service.
Click Generate Domain to create a public URL for your app.




## make 


# final requirements.txt 



´´´
asgiref==3.8.1
Django==5.1.5
psycopg2-binary==2.9.6
sqlparse==0.5.3
tzdata==2025.1
whitenoise==6.8.2
dj-database-url==2.3.0
gunicorn==20.1.0

´´´

curl -fsSL https://railway.com/install.sh | sh
railway link -p 5c612e60-5712-4138-8f02-a051834a1838









