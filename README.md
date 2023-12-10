# 29maktab.uz backend
The backend of the 29maktab.uz site built on the django framework

### Aequence of steps
- [Installation (Docker)](#installation-docker)
- [Installation (without Docker)](#installation)
- [Installation PostgresSQL (Docker)](#installation-postgressql-docker)
- [Installation PostgresSQL (without Docker)](#installation-postgressql)
- [Run app](#run-app)


### Installation (Docker)
1. First you need to download docker
2. Run docker
3. Open the project folder
4. Run a command on terminal
    ```bash 
    $ docker compose up --build
    ```
### Installation
1. Install python 3.10 version
2. Install pip
3. Open the project folder
4. Run a commands on terminal:
    ```bash 
    $ pip install -r requirements.txt
    ```
    ```bash
    $ python manage.py migrate
    ```
    ```bash
    $ python manage.py runserver
    ```
### Installation PostgresSQL (Docker)
1. Open the settings.py file in config folder
2. Paste this code:
   ```bash
   DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env("POSTGRES_DB"),
            'HOST': env('POSTGRES_HOST'),
            'PORT': env("POSTGRES_PORT"),
            'USER': env('POSTGRES_USER'),
            'PASSWORD': env('POSTGRES_PASSWORD'),
        }
    }
   ```
4. Run a commands on terminal:
   ```bash
   $ docker exec -it school_db_1 psql -U postgres
   ```
5. Once you are in the PostgreSQL interactive terminal, run the following SQL command to create the "your_data_base" database:
   ```bash
   $ CREATE DATABASE yourdatabasename;
   ```
   Replace yourdatabasename with the desired name for your database.

6. Apply the migrations:
   ```bash
   $ docker-compose run school_web_1 python manage.py migrate
   ```
### Installation PostgresSQL
1. Access PostgreSQL:
   * Use a PostgreSQL client, such as ' psql ', to connect to your PostgreSQL server.
     
2. Run SQL Query:
   ```bash
   CREATE DATABASE yourdatabasename;
   ```
   Replace yourdatabasename with the desired name for your database.
   
4. Open the settings.py file in config folder

5. Paste this code:
   ```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env("POSTGRES_DB"),
            'HOST': 'localhost',
            'PORT': env("POSTGRES_PORT"),
            'USER': env('POSTGRES_USER'),
            'PASSWORD': env('POSTGRES_PASSWORD'),
        }
    }
   ```
   
6. Run a commands on terminal:
   ```bash
   $ python manage.py makemigrations
   ```
   ```bash
   $ python manage.py migrate
   ```

### Run app (Docker)
1. Run a commands on terminal:
   ```bash
   $ docker compose up
   ```

### Run app
1. Run a commands on terminal:
   ```bash
   $ python manage.py createsuperuser
   ```
   ```bash
   $ python manage.py runserver
   ```
