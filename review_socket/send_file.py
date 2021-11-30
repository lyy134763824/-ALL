from socket import *
server_addr = ('127.0.0.1',8888)


s = socket()
f = open('test.jpg','rb')
s.connect(server_addr)
while True:
    data = f.read()
    if not data:
        break
    s.send(data)
    # data = s.recv(1024*1024)
    # print(f'receive data:{data.decode()}')

s.close()