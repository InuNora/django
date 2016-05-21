#!/bin/bash

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
cp /home/box/stepic/gunicorn.ask /home/box/web/etc/gunicorn.ask
sudo ln -sf /home/box/web/etc/gunicorn.ask /etc/gunicorn.d/test/gunicorn.conf
sudo /etc/init.d/gunicorn restart
