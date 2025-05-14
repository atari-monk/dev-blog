# Django Structure

## Default Project Layout

Running `django-admin startproject projectname` generates:

```
projectname/
│
├── projectname/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── manage.py
```

## Core Files

- **manage.py**
  - CLI tool for development tasks
  - Run server, execute migrations, create apps

- **settings.py**
  - Project configuration
  - Databases, apps, middleware, templates
  - `SECRET_KEY` for production

- **urls.py**
  - URL routing definitions

- **wsgi.py** / **asgi.py**
  - Production server entry points

- **__init__.py**
  - Python package marker

## App Structure

Running `python manage.py startapp appname` creates:

```
projectname/
│
├── appname/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── projectname/
└── manage.py
```