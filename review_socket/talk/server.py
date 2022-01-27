
from socket import  *
import os,sys

ADDR= ("0.0.0.0",8888)

#存储用户信息
user = {}

def do_login(s,name,addr):
    if name  in user or "管理员" in user:
        s.sendto('该用户存在'.encode(),addr)
        return
    s.sendto(b'OK',addr)
    #通知其他人信息
    msg = f'欢迎{name}进入聊天室'
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
    user[name] = addr

def do_talk(s,name,msg):
    msg = "\n" + name + ":" + msg
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_quite(s, name):
    msg = f'{name}推出聊天室,'
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b'EXIT', user[i])
    # del user[name]

def get_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        print(data.decode())
        # 2表示最多切割2项
        tmp = data.decode().split(' ',2)
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr)
        elif tmp[0] == 'M':
            if tmp[2] == '':
                continue
            # print(tmp[1],tmp[2])
            do_talk(s,tmp[1],tmp[2])
        elif tmp[0] == 'Q':
            if tmp[1] in user:
                do_quite(s, tmp[1])

def main():
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid <0:
        print('Error')
    elif pid == 0:
        while True:
            msg = input("管理员消息：")
            msg = "M 管理员 "+msg
            s.sendto(msg.encode(),ADDR)
    else:
        get_request(s)


if __name__ == '__main__':
    main()














































