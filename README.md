App  que permite dar de alta productos con valores nutricionales
-----------------------------------------------------------------------
version: V1.
idioma: en

user: django
pss: django1234

Instalar Python 3.7 o superior en local
Instalar Django 2.2.7 en entorno virtual

Instalar pip para python3
---------------------------------
sudo apt install python3-pip

--------------------------------------
Opcion 1:
--------------------------------------
Instalar entorno virtual en windows
--------------------------------------
pip3 install pipenv

Instalar decouple
--------------------------------------
pipenv install python-decouple

Instalar django filter
------------------------------------
pipenv install django-filter

Instalar gunicorn para heroku
----------------------------------------------------------
pipenv install dj-database-url gunicorn whitenoise

Activar entorno virtual
----------------------------------------
pipenv shell

Instalar Django
----------------------------------------
pipenv install Django==2.2.7

Instalar conexión postgresql
----------------------------------------
pipenv install psycopg2


-------------------------------------------------
Opcion 2:
-------------------------------------------------
Instalar entorno virtual (virtualenv) en linux
-------------------------------------------------
sudo apt install python3-virtualenv

Crear entorno virtual
-----------------------------------------------
virtualenv entorno_virtual -p python3

Activar entorno virtual
-----------------------------------------------
source entorno_virtual/bin/activate

Desativar entorno virtual
-----------------------------
desativate





Instalar decouple
--------------------------------------
pip3 install python-decouple

Instalar django filter
------------------------------------
pip3 install django-filter

Instalar gunicorn para heroku
----------------------------------------------------------
pip3 install dj-database-url gunicorn whitenoise

Instalar Django
----------------------------------------
pip3 install Django==2.2.7

Instalar conexión postgresql
----------------------------------------
sudo apt-get install python3-psycopg2
pip install psycopg2-binary

----------------------------------------
Crear el projecto
----------------------------------------
django-admin startproject cms
cd cms

Crear App
----------------------------------------
python manage.py startapp products

Añadir la app al settings

Crear el modelo y relaciones en postgres
-----------------------------------------
sudo -u postgres psql
create user javier with encrypted password '2525_ap';
alter user javier createdb;
create database products;


Hacer migraciones de tablas de la BBDD
--------------------------------------------
python manage.py makemigrations
python manage.py migrate

Crear usuario administrador
--------------------------------------------
python manage.py createsuperuser
user: django
pss: django1234



Ejecutar el  servidor
--------------------------------------------
python manage.py runserver
http://127.0.0.1:8000/

Crear views.py en la App

Añadir el path de la vista a urls.py



