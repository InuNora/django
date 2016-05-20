#!/bin/bash

gunicorn -c /home/box/web/etc/hello.py -b 0.0.0.0:8080 hello:application &
# gunicorn - b 0.0.0.0:8080 hello:application &

cd /home/box/web/ask/ask
gunicorn -c /home/box/web/etc/hello.py -b 0.0.0.0:8000 wsgi:application &
# gunicorn - b 0.0.0.0:8000 wsgi:application &
