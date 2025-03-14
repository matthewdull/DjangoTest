Django Project Overview:

- Create a project directory and a virtual environment for the project:
    - Virtual environment: a lens on how to look at our project and what packages we have installed (isolates packages for this project)
    - python -m venv .venv      (create a virtual environment named ".venv")
    - . .venv/Scripts/activate  (activate the venv)
    - pip freeze                (returns all the additional packages we installed)
    - deactivate                (deactivate the venv)

- Install packages:             (pip is the default package manager for Python for managing packages from the Python Package Index PyPI)
    - pip install django        (install Django package)

- Create Django Project:
    - django-admin --help                   (show us the different commands we can create)
    - django-admin startproject movies .    (creates the Django project directory called movies, . is for current directory)

- Add Git repository:
    - install git at git-scm.com/downloads
    - git init               (initialize a new git repository)
    - add .gitignore file    (anything in this file will be ignored in git repo)
    - can use a thorough gitignore found online for Django
    - git add *
    - git commit -m "Initial Django Project Setup"
    - git push
