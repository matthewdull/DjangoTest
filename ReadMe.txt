Django Project Overview:

- Create a project directory and a virtual environment for the project:
    - Virtual environment: lens on how to look at our project and what packages we installed (isolates packages for this project)
    - python -m venv .venv      (create a virtual environment named ".venv")
    - . .venv/Scripts/activate  (activate the venv)
    - pip freeze                (returns all the additional packages we installed)
    - deactivate                (deactivate the venv)

- Install packages:           (pip is the default package manager for Python for managing packages from the Python Package Index PyPI)
    - pip install django      (install Django package)

- Create Django Project:
    - django-admin --help                  (show us the different commands we can create)
    - django-admin startproject movies .   (creates the Django project directory called movies, . is for current directory)

- Add Git repository (source control):
    - install git at git-scm.com/downloads
    - git init               (initialize a new git repository)
    - add .gitignore file    (anything in this file will be ignored in git repo)
    - can use a thorough gitignore found online for Django
    - git add *
    - git commit -m "Initial Django Project Setup"
    - Go to Github and create new repository and copy terminal input to add remote and set up main branch
----------------------------------------------------------------------------------------------------------
PROJECT SETUP DONE!
----------------------------------------------------------------------------------------------------------
- Structuring Django Applications (MVT):
    - Model: Representation/Structure of your data.
    - View: What accetps requests and gets the appropriate data.
    - Template: Visual page structure being sent to the client.

- Setting up "hello world" equivalent in Django:
    - Create the most basic View that just reponds to a request.
    - Use the manage.py file to do anything related to managing our server
    - python manage.py runserver  (start local web server (urls.py already has admin site path))
    - Add new site path to urls.py called movies: path('movies/', views.movies)
    - create views.py in project directory and in urls.py add "from movies import views"
    - In views.py, "from django.http import HttpResponse"
    - Define first view (function) that upon recieving a request, sends HttpResponse "Hello there"
    - Do there same for creating a new "home" view and corrresponding site path