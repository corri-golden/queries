# Queries

QUERIES was developed for novelists looking for agents to publish their book.  The app allows the novelists to keep their mulitple query (250 word description of the novel sent to agents) statuses organized. After creating a query card with the agent's information, the user can move the query cards between three columns pending, followup, and rejected so they will always know what the statuses of their queries in one page.

## Technologies Used
Queries was developed using the following:
1.  Python  
2.  Django framework.
3.  Sqlite
4.  ORM
5.  Bootstrap


## Instructions for installing Queries
Clone this repo using the following command then cd into it

- git clone git@github.com:corri-golden/queries.git
- cd queries

#### For Mac users: create your virtual environment in Terminal

- python -m venv queriesenv
- source ./queriesenv/bin/activate

#### For Windows users: create your virtual environment in Command Line

- python -m venv workforceenv
- source ./workforceenv/Scripts/activate

### Install the app's dependencies

- pip install -r requirements.txt

### Build your database from the existing models

- python manage.py makemigrations queriesapp
- python manage.py migrate

### Create a superuser for your local version of the app

- python manage.py createsuperuser

### Populate your database with initial data from fixtures files: (NOTE: every time you run this it will remove exisiting data and repopulate the tables)

python manage.py loaddata query
python manage.py loaddata book
python manage.py loaddata agent
python manage.py loaddata status

### Run your dev server

- python manage.py runserver



