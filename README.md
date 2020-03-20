# Queries

QUERIES was developed for novelist who are looking for agents to publish their book.  The app allows the novelist to organize the queries (250 word description of the novel sent to agents). After creating a query card with the agent's information, the user can drag and drop the query between three columns pending, followup, and rejected so they will always know what the statuses of their queries in one page.

Technologies Used
Queries was written in Python with the Django framework.

Queries was developed using VSCode, GitHub, ORM, and TablePlus

Instructions for installing Queries
Clone this repo using the following command then cd into it

git clone github.com/corri-golden/queries.git

For Mac users: create your virtual environment in Terminal

python -m venv queriesenv
source ./queriesenv/bin/activate

For Windows users: create your virtual environment in Command Line

python -m venv workforceenv
source ./workforceenv/Scripts/activate

Install the app's dependencies

pip install -r requirements.txt

Build your database from the existing models

python manage.py makemigrations queriesapp
python manage.py migrate

Create a superuser for your local version of the app

python manage.py createsuperuser

Populate your database with initial data from fixtures files: (NOTE: every time you run this it will remove exisiting data and repopulate the tables)

python manage.py loaddata query
python manage.py loaddata book
python manage.py loaddata agent
python manage.py loaddata status

Run your dev server

python manage.py runserver



