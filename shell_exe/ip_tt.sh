#!/bin/bash


for i in {2..254}
do 
	ping -c 2 127.0.0.$i &> /dev/null
        if [ $? -eq 0 ];then
		echo "127.0.0.$i可用"
	else
		echo "127.0.0.$i不可用"
	fi

done
