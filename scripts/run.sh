#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

python manage.py collectstatic --noinput
python manage.py migrate

python manage.py runserver 0.0.0.0:8005