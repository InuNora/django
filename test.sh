#!/bin/bash

curl -I http://127.0.0.1/login/
curl -I http://127.0.0.1/?page=2
curl -I http://127.0.0.1/popular/?page=2
curl -I http://127.0.0.1/question/3141592/