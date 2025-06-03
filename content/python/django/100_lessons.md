# 100 Django Lessons

## Lesson 1

Absolutely! Here's a carefully sequenced 100-step curriculum to teach you **Django**, from beginner to advanced, with each lesson building on the previous. Let's begin with **Lesson 1**.

---

### ✅ **Django in 100 Lessons**

**Lesson 1: Introduction & Environment Setup**

---

#### 🎯 Objective:

Understand what Django is and set up your development environment.

---

### 🔹 What is Django?

* Django is a **high-level Python web framework**.
* It encourages **rapid development** and **clean, pragmatic design**.
* Built by experienced developers to take care of the hassle of web development.

---

### 🔹 Why Use Django?

* Fast development.
* Secure by default (protects against common threats like XSS, CSRF, SQL injection).
* Scalable & flexible.
* Rich ecosystem and community.
* Admin interface, ORM, URL routing, forms, and more — built-in.

---

### 🔹 Prerequisites

* Basic knowledge of Python (functions, classes, packages).
* Comfortable using command line / terminal.

---

### 🔹 Step-by-Step Setup

#### 1. 🔧 Install Python (if not already installed)

Make sure Python 3.8+ is installed:

```bash
python --version
```

If not installed, download from [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

#### 2. 💼 Create a Virtual Environment

Navigate to your project folder and run:

```bash
python -m venv django_env
```

Activate the virtual environment:

* **Windows:**

```bash
django_env\Scripts\activate
```

* **macOS/Linux:**

```bash
source django_env/bin/activate
```

---

#### 3. 📦 Install Django

```bash
pip install django
```

Verify installation:

```bash
django-admin --version
```

---

#### 4. 🚀 Create Your First Django Project

```bash
django-admin startproject mysite
cd mysite
```

To run the development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser – you’ll see the Django welcome page!

---

✅ **You’ve just set up your first Django project!**
When you're ready, type **`n`** to proceed to **Lesson 2: Django Project Structure**.

## Lesson 2

Great! Let’s move on.

---

### ✅ **Lesson 2: Django Project Structure**

---

#### 🎯 Objective:

Understand the files and folders Django creates when you start a project.

---

### 🗂️ After running `django-admin startproject mysite`, this is what you get:

```
mysite/
├── manage.py
└── mysite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

### 🔍 Breakdown of Each File:

#### 1. `manage.py`

* A command-line tool to interact with your Django project.
* Used to run the server, create apps, run migrations, open the shell, etc.
* Example:

```bash
python manage.py runserver
python manage.py migrate
```

---

#### 2. `mysite/` (inner folder)

This is the actual Python package for your project. It has the **settings** and **configuration** for your whole Django project.

* **`__init__.py`**

  * Empty file that tells Python this folder is a package.

* **`settings.py`**

  * The heart of your project.
  * Contains configurations: installed apps, middleware, database, static files, etc.

* **`urls.py`**

  * Defines the **URL patterns** for the project.
  * Controls what happens when a user visits a specific route.

* **`asgi.py` / `wsgi.py`**

  * Entry points for ASGI and WSGI servers (used for deploying Django).
  * You won't touch these often as a beginner.

---

### 🔧 Run the Server (Recap)

From the outer `mysite/` directory:

```bash
python manage.py runserver
```

Then open your browser to:

```
http://127.0.0.1:8000/
```

You’ll see the default Django welcome page.

---

✅ That’s your Django project skeleton.
When you're ready, type **`n`** to proceed to **Lesson 3: Creating a Django App**.

## Lesson 3

Perfect — let’s dive in.

---

### ✅ **Lesson 3: Creating a Django App**

---

#### 🎯 Objective:

Understand what a Django **app** is and create your first one.

---

### 📦 What’s a Django App?

* A Django **project** is made up of one or more **apps**.
* An app is a **modular component** (like blog, store, users).
* Reusable across projects.
* You can think of a project as the whole website and apps as parts of it.

---

### 🛠️ Create Your First App

Let’s say you want to build a blog system.

#### From the project root (`mysite/`), run:

```bash
python manage.py startapp blog
```

This creates a folder like this:

```
blog/
├── admin.py
├── apps.py
├── __init__.py
├── migrations/
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

---

### 🔍 Breakdown of Files:

* **`admin.py`** – Register models here to make them appear in Django admin.
* **`apps.py`** – Configuration for the app.
* **`models.py`** – Define your data models (tables).
* **`views.py`** – Handle logic for HTTP requests.
* **`migrations/`** – Stores migration files to update your database schema.
* **`tests.py`** – Write unit tests here.

---

### 🧠 Don’t Forget: Activate the App!

Open `mysite/settings.py` and add your app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'blog',
]
```

---

✅ You’ve just created your first Django app and hooked it into your project.

When you're ready, type **`n`** to proceed to **Lesson 4: Creating Your First View**.

## Lesson 4

Awesome, let’s continue.

---

### ✅ **Lesson 4: Creating Your First View**

---

#### 🎯 Objective:

Create a simple view that returns a response when someone visits a URL.

---

### 🧱 What is a View?

A **view** is a Python function or class that takes a **request** and returns a **response**.

Most common response types:

* Plain text (`HttpResponse`)
* HTML templates (`render`)
* JSON (`JsonResponse`)

---

### 🛠️ Create a Basic View

Open `blog/views.py` and add this:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is the blog homepage!")
```

This is your first Django view!

---

### 🔗 Connect the View to a URL

1. **Create a file `blog/urls.py`** (if it doesn’t exist):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

2. **Include `blog.urls` in the project `urls.py`:**

Open `mysite/urls.py` and modify it:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Root URL goes to blog app
]
```

---

### ▶️ Test It

Run the server if it’s not already running:

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

✅ You should see:

```
Hello, this is the blog homepage!
```

---

You're now handling HTTP requests — a major milestone!

Type **`n`** to proceed to **Lesson 5: Django URL Routing Deep Dive**.

## Lesson 5

Great pace! Let’s dive deeper.

---

### ✅ **Lesson 5: Django URL Routing Deep Dive**

---

#### 🎯 Objective:

Understand how Django routes URLs to the correct views and how to organize them properly.

---

### 🔁 What is URL Routing?

* When a user visits a URL, Django looks for a **matching pattern** in `urls.py`.
* If a match is found, Django **calls the view function** associated with it.
* If no match is found, it returns a **404 error**.

---

### 🧭 Anatomy of a URL Pattern

In `blog/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

* `''` means the **root** of this app (e.g., `/`).
* `'about/'` matches `/about/`.
* `views.about` is the function called.
* `name='about'` allows you to refer to this URL elsewhere (e.g., in templates).

---

### 🧪 Add Another View

In `blog/views.py`, add:

```python
def about(request):
    return HttpResponse("This is the about page.")
```

Now, if you visit:

```
http://127.0.0.1:8000/about/
```

You should see:

```
This is the about page.
```

---

### 🧩 URL Namespacing (Preview)

If you had multiple apps, you might **namespace** your URLs to avoid name clashes.

Example:

```python
app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
]
```

Then in templates:

```html
<a href="{% url 'blog:home' %}">Home</a>
```

(We’ll go deeper into templates soon.)

---

✅ You now understand how Django maps URL paths to view functions.
When you're ready, type **`n`** to continue to **Lesson 6: Django Templates – Rendering HTML**.

## Lesson 6

You're moving fast — awesome! Let’s render real HTML.

---

### ✅ **Lesson 6: Django Templates – Rendering HTML**

---

#### 🎯 Objective:

Learn how to return proper HTML pages using Django’s **template system** instead of plain text.

---

### 🧠 What is a Template?

* A **template** is an HTML file with **Django template language (DTL)** features.
* It lets you dynamically insert data from your views.

---

### 📁 Step 1: Create a Templates Folder

Inside your `blog/` app, create this structure:

```
blog/
└── templates/
    └── blog/
        ├── home.html
        └── about.html
```

**Note**: You can name the inner folder `blog` to match the app name — helps avoid name collisions across apps.

---

### 📝 Step 2: Add HTML Files

**`home.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Blog Home</title>
</head>
<body>
    <h1>Welcome to the Blog!</h1>
</body>
</html>
```

**`about.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>About</title>
</head>
<body>
    <h1>About This Blog</h1>
    <p>This blog is made with Django!</p>
</body>
</html>
```

---

### 🔁 Step 3: Update Views to Render Templates

**In `views.py`:**

```python
from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')
```

---

### ⚙️ Step 4: Ensure Templates Folder is Recognized

In `settings.py`, make sure the `DIRS` section in `TEMPLATES` looks like this:

```python
'DIRS': [],
```

This is fine for now since Django auto-detects templates inside app folders.

---

### ✅ Final Test

Restart your server (if needed):

```bash
python manage.py runserver
```

Visit:

* [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* [http://127.0.0.1:8000/about/](http://127.0.0.1:8000/about/)

🎉 You’re now rendering real HTML pages with Django’s template engine!

---

Type **`n`** to continue to **Lesson 7: Template Inheritance – DRY Your HTML**.

## Lesson 7

Excellent! You're now ready to clean up and reuse your HTML.

---

### ✅ **Lesson 7: Template Inheritance – DRY Your HTML**

---

#### 🎯 Objective:

Use Django’s **template inheritance** system to avoid repeating HTML boilerplate across pages.

---

### 🧱 Problem:

Right now, `home.html` and `about.html` repeat the same:

```html
<!DOCTYPE html>
<html>
<head>
    ...
</head>
<body>
    ...
</body>
</html>
```

This violates **DRY**: *Don’t Repeat Yourself*.

---

### 🛠️ Step 1: Create a Base Template

Create a new file:

```
blog/templates/blog/base.html
```

Add this content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Blog{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Blog</h1>
        <nav>
            <a href="/">Home</a> |
            <a href="/about/">About</a>
        </nav>
        <hr>
    </header>

    {% block content %}
    {% endblock %}
</body>
</html>
```

---

### 🪄 Step 2: Update `home.html` and `about.html`

**`home.html`:**

```html
{% extends 'blog/base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <h2>Welcome to the Blog!</h2>
{% endblock %}
```

**`about.html`:**

```html
{% extends 'blog/base.html' %}

{% block title %}About{% endblock %}

{% block content %}
    <h2>About This Blog</h2>
    <p>This blog is made with Django!</p>
{% endblock %}
```

---

### 🔁 Recap

* `base.html` is the master layout.
* Other templates **extend** it and define their own content inside `{% block %}` tags.
* Easier to maintain consistent layouts.

---

✅ Now you have **reusable templates** and a clean project structure.

Type **`n`** to continue to **Lesson 8: Static Files – CSS, JS, and Images in Django**.

## Lesson 8

You're doing great — now let's add style!

---

### ✅ **Lesson 8: Static Files – CSS, JS, and Images in Django**

---

#### 🎯 Objective:

Learn how to add and use **static files** like CSS, JavaScript, and images in your Django project.

---

### 📁 Step 1: Create a Static Folder in Your App

Inside your `blog/` directory, create:

```
blog/
└── static/
    └── blog/
        └── styles.css
```

> You should now have: `blog/static/blog/styles.css`

---

### 🖌️ Step 2: Add Some CSS

**`styles.css`**

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    margin: 20px;
}

h1 {
    color: #0077cc;
}
```

---

### ⚙️ Step 3: Configure Static Settings (Optional)

Open `settings.py` and confirm these values exist:

```python
STATIC_URL = '/static/'
```

> Django uses this to serve static files in development.

---

### 🧪 Step 4: Use the Static File in Templates

At the top of your templates (e.g., `base.html`), load the static template tag:

```django
{% load static %}
```

Then add this inside `<head>`:

```html
<link rel="stylesheet" href="{% static 'blog/styles.css' %}">
```

---

### 🧠 Notes:

* During development, Django serves static files automatically.
* In production, you need to collect and serve them with a web server (we'll cover that later).

---

### ▶️ Final Test

Restart server (if needed) and refresh your site:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` – your site should now have improved styling!

---

✅ You now know how to serve CSS and static assets in Django.

Type **`n`** to move on to **Lesson 9: Django Models – Creating Database Tables**.

## Lesson 9

## Lesson 10

## Lesson 11

## Lesson 12

## Lesson 13









