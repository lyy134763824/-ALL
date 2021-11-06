#!/bin/bash


read -p "请选择操作(start|stop|restart):" op

case $op in 
  "start")
  sudo /etc/init.d/nginx start
  ;;
 "stop")
 sudo /etc/init.d/nginx stop
 ;;
 "restart")
 sudo /etc/init.d/nginx restart
 ;; 
 *)
	 echo "输入不正确"

esac
