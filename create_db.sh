#!/usr/bin/env bash

/etc/init.d/mysql restart

mysql -u root -e "create user 'ask'@'localhost' identified by 'ask'"
mysql -u root -e "create database ask default character set=utf8"
mysql -u root -e "grant all privileges on ask. * to 'ask'@'localhost'"
mysql -uroot -e "FLUSH PRIVILEGES;"

# mysql -uroot -e "CREATE DATABASE djbase;"
# mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY 'pass123';"
# mysql -uroot -e "GRANT ALL ON djbase.* TO 'django@localhost';"
# mysql -uroot -e "FLUSH PRIVILEGES;"


cd ask/
# manage.py startapp qa

# mysql -u ask -p ask -e "alter table qa_question modify column added_at date default null"
python manage.py syncdb
