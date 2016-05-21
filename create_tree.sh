#!/bin/bash

cp -r /home/box/stepic/web/ /home/box/

cd /home/box/web/
django-admin startproject ask
cd /home/box/web/ask/
django-admin startapp qa
