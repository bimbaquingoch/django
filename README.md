<h1 align="center">Django 👋</h1>

## Create virtualenv

```sh
pipenv install django
```

## Activate virtualenv

```sh
pipenv shell
```

## Create a Django project

```sh
django-admin startproject project_name dir_path
```

## Run django

```sh
python manage.py runserver
```

## Create package

```sh
python manage.py startapp package_name
```

## Create database file

```sh
python manage.py migrate
```

## Create super-user

```sh
python manage.py createsuperuser
```

## Login super-user

> go to 127.0.0.1:8000/admin and then sing in with credentials created in the previous step

## Show all installed packages

```sh
pip freeze
```

## Create model package

```sh
python manage.py makemigrations
<!-- example -->
python manage.py makemigrations
python manage.py migrate
```

> Now in 127.0.0.1:8000/admin you can create new Model
