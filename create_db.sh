#!/bin/bash

# run as sudo

/etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE qa; CREATE USER 'qa'@'%' IDENTIFIED BY '123456'; GRANT ALL PRIVILEGES ON qa.* TO 'qa'@'%';"

#pip install pymysql


#mysql -uroot -e "CREATE DATABASE box_django;"
#mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
#mysql -uroot -e "GRANT ALL PRIVILEGES ON box_django.* TO 'box'@'localhost';"
#mysql -uroot -e "FLUSH PRIVILEGES;"

#mysql -uroot -e "CREATE DATABASE stepic_web;"
#mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"
