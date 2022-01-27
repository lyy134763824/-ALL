'''

客户端

'''

from socket import *
import sys,os



ADDR = ("127.0.0.1",8888)

def send_msg(s,name):
    while True:
        try:
            msg = input('请输入内容:')
        except KeyboardInterrupt:
            msg = 'Q ' + name
            s.sendto(msg.encode(), ADDR)
            sys.exit('退出聊天室')
        if msg == 'Q':
            msg = 'Q '+name
            s.sendto(msg.encode(),ADDR)
            sys.exit('退出聊天室')
            # return
        text = f"M {name} {msg}"
        s.sendto(text.encode(),ADDR)

def recv_msg(s):
    while True:
        data, addr = s.recvfrom(4096)
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+"\n发言：",end='')


def main():
    s = socket(family=AF_INET,type=SOCK_DGRAM)
    while True:
        name = input('请输入名字：')
        msg = 'L '+name
        s.sendto(msg.encode(),ADDR)
        data,addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print('进入聊天室')
            break
            # while True:
            #     data, addr = s.recvfrom(128)
            #     print(data.decode())
            #     msg = input('请输入内容：\n')
            #     if msg == 'Q':
            #         msg = 'Q '
            #         s.sendto(msg.encode(),ADDR)
            #         return
            #     else:
            #         msg = f'M {name} '+msg
            #         s.sendto(msg.encode(), ADDR)
        else:
            print(data.decode())
    pid = os.fork()
    if pid < 0:
        print('Error')
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)

if __name__ == '__main__':
    main()







