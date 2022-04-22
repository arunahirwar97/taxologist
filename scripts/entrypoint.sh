#!/bin/sh

set -e
python manage.py collectstatic --noinput
python manage.py wait_for_db
# find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# find . -path "*/migrations/*.pyc"  -delete
# python manage.py makemigrations
# find . -path "*/migrations/*.pyc" 
# find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# find . -path "*/__pycache__/*.pyc" 
# python manage.py makemigrations
# python manage.py migrate
# python manage.py mikemigrations --merge 
python manage.py migrate 

uwsgi --socket :9000 --workers 4 --master --enable-threads --module core.wsgi


