import socket
from socket import  *

#AF_INET:IP_V4  SOCK_STREAM流式  SOCK_DGRAM 报式 proto子协议
# socket.AF_INET,\socket.SOCK_STREAM

ss = socket(family=AF_INET,type=SOCK_STREAM,proto=0)
ss.bind(('127.0.0.1',8888))
#监听多少个 大小  超过10个客户端报错
ss.listen(10)
f = open('tt.jpg','wb')
while True:
    print('Wating for connect ..')
    try:
        ss2,addr = ss.accept()
    except KeyboardInterrupt:
        print('Server is exit')
        break
    print(f'Connection addr :{addr}')
    while True:
        # ss2 一个新的套接字  addr 客户端链接的地址
        #bufsize= 一次最多接受多少字节  字节串
        data = ss2.recv(1024*1024)

        f.write(data)


        #n 实际发送的字节数
        # data2 = b'Thanks'
        # n = ss2.send(data2)
    ss2.close()


ss.close()





