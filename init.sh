#!/bin/bash

mkdir -p /home/box/web/{etc,uploads,public}/
mkdir -p /home/box/web/public/{img,js,css}/

cp /home/box/stepic/nginx.conf /home/box/web/etc/nginx.conf
cp /home/box/stepic/hello.py /home/box/web/hello.py
cp /home/box/stepic/etc/hello.py /home/box/web/etc/hello.py

# cd /home/box/web/
# django-admin startproject ask
# cd /home/box/web/ask/
# django-admin startapp qa

cp /home/box/stepic/views.py /home/box/web/ask/qa/views.py
cp /home/box/stepic/urls.py /home/box/web/ask/qa/urls.py

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
gunicorn - b 0.0.0.0:8080 hello:application &
gunicorn - b 0.0.0.0:8000 wsgi:application &

sudo /etc/init.d/gunicorn restart
