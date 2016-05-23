#!/usr/bin/env bash

# run as sudo
apt-get update
apt-get install -y Nginx
apt-get install -y gunicorn
apt-get install -y python-pip
pip install Django==1.6.1
apt-get install mc
apt-get install mysql-server

ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart

gunicorn -c /home/box/web/etc/hello.py hello:application --daemon
gunicorn -c /home/box/web/etc/django.py wsgi --daemon

/etc/init.d/mysql start
