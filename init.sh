#!/bin/bash

mkdir -p /home/box/web/{etc,uploads,public}/
mkdir -p /home/box/web/public/{img,js,css}/

cp /home/box/stepic/nginx.conf /home/box/web/etc/nginx.conf
cp /home/box/stepic/hello.py /home/box/web/hello.py
cp /home/box/stepic/etc/hello.py /home/box/web/etc/hello.py

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
