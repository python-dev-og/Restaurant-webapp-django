## Create the project and application folders
```
django-admin startproject mysite .
python manage.py startapp restaurant_menu
```
## Connect the Application 

connect the application `restaurant_menu` to the project folder `mysite`'
Add `restaurant_menu` to the  INSTALLED_APPS [] block in the `mysite/settings.py`
 
## To run the application

```commandline
python manage.py runserver
```
## Design the database Model

Enter the database models on `restaurant_menu/models.py`

```commandline
 python manage.py makemigrations
 python manage.py migrate
```

## Create Views for our Models

create class in `restaurant_menu/views.py`

create html file in `restaurant_menu/templates/index.html`
create urls file in `restaurant_menu/urls.py`
create class file in `restaurant_menu/forms.py`

## Create a user for the admin page
```commandline
python manage.py createsuperuser
```
follow the prompt 