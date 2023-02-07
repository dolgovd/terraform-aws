#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
echo "<html><h1>Hello World</h1></html>" > /var/www/html/index.html
yum install -y amazon-efs-utils