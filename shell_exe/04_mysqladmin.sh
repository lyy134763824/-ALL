#! /bin/bash

user="lyy"
passwd="123"

while :
do
	count=`mysqladmin -u$user -p$passwd status | awk '{print $4}'`
	echo "`date +%y-%m-%d`--`date +%H:%M:%S`并发连接数为: $count "
	sleep 2

done

