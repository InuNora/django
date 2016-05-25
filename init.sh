#!/bin/bash

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#gunicorn -c /home/box/web/etc/hello.py hello:application --daemon
#gunicorn -c /home/box/web/etc/django.py wsgi --daemon

python /home/box/web/ask/manage.py runserver 0.0.0.0:8000 &
