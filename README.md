# meme_machine

Meme Machine, project for CS474. 

TEAM - Justice League

Dev install instructions:
MySQL, NPM, and Python3.8 are required, each of the steps for them are detailed below.


MySQL:
(Make sure you're in SQL mode, not JavaScript (JS) by running \sql)
Run the following commands to create a new database, and add a new user to said database. 


DATABASE
-----------
\sql
CREATE DATABASE meme_machine;
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;


Backend
-----------

Using the pip module in python, install 'pipenv'. ("python -m pip install pipenv", or simply "pip install pipenv" if pip is on your path)
In your meme_machine directory, run 'pipenv shell'. This will access a python virtual environment. 
Now, run 'pipenv sync' to download the necessary dependencies for your virtual environment from the Pipfile.lock.
Note: Always load back into this virtual environment when doing backend work, in order to avoid issues with dependencies.

Now, in your /meme_machine/backend/backend directory, with the manage.py, run the following. This will migrate the changes to the database, and start the server.

python manage.py migrate
python manage.py runserver


For accessing the admin panel, located at 'localhost:8000/admin', you need to create a user in the database. This can be done with the following command:

python manage.py createsuperuser

Now, you should be capable of logging into 'localhost:8000/admin'.


Frontend
-----------
For the Front-end portion, navigate to meme_machine/frontend. 
In this directory run 'npm install'. This will fill the node_modules file with the necessary npm packages.
Now that the packages have been installed run 'npm run serve' to serve the static files. 
You can now navigate to localhost:8080, in order to test and use the frontend components. 