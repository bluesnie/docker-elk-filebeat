#!/bin/bash

echo "=================migrate================="
python manage.py makemigrations&&
python manage.py migrate&&

echo "=================start uwsgi================="
uwsgi --ini /opt/python_project/app/uwsgi.ini
