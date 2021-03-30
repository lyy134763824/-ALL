
echo "number:$#" 
echo "scname:$0" 
echo "first :$1" 
echo "second:$2" 
echo '     -----$*'
for i in "$*"; do
    echo $i
    done
 
echo '     -----$@'
for i in "$@"; do
    echo $i
    done
echo "PID:$$"
 
#bash test.sh aa bb cc
#————————————————
#版权声明：本文为CSDN博主「-纸短情长」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声#明。
#原文链接：https://blog.csdn.net/l_liangkk/article/details/105649018
