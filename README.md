-   Install python

-   How to create a virtual environment:

    -   Python3 -m venv \<env_name\>

    -   Cd \<env_name\>

    -   Source bin/activate

    -   Deactivate -- to exit virtual env

-   How to create a django project

    -   Django-admin startproject \<project_name\>

-   How to run a server in django

    -   Python3 manage.py runserver

-   How to stop a running server

    -   pkill -f runserver

-   What if I want to run server at some different port number

    -   Python manage.py runserver \<port_number\>

-   How to create an app in django

    -   Python3 manage.py startapp \<app_name\>

-   How to connect postgresql to django

    -   Need to make changes in settings.py Name,User,Password,Host,Port

    -   Install connector pip3 install psycopg2

-   How to do the migration in django

    -   Python3 manage.py makemigration

    -   Python3 manage.py migrate

-   How to create a url

    -   Create a file named urls.py and set the url

    -   Then add the app level urls to the main url.py
