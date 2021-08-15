# Django Backend

Commands used since the start of project:

## Initialize Django project

```console
cd backend
django-admin startproject backend .

```

### Start a new application called `todo`

```console
python manage.py startapp todo

```

### Run migrations

```console
python manage.py migrate
```

### Start up the server

```console
python manage.py runserver
```

## Database Migrations after Defining the `Todo` Model

```console
python manage.py makemigrations todo
python manage.py migrate todo
```

## Create Superuser for Admin Interface

```console
python manage.py createsuperuser
python manage.py runserver
```
Navigate to http://localhost:8000/admin in your web browser.

## Setting Up the APIs

Install the `djangorestframework` and `django-cors-headers`:

```console
pip install djangorestframework django-cors-headers

```

`django-cors-headers` is a Python library that will prevent the errors that you would normally get due to CORS rules. In the `CORS_ORIGIN_WHITELIST` code, you whitelisted `localhost:3000` because you want the frontend (which will be served on that port) of the application to interact with the API.

