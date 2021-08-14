# Django Backend

Commands used since the start of projects:

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