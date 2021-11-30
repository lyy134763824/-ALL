from socket import *
server_addr = ('127.0.0.1',8889)


s = socket()

s.connect(server_addr)
while True:
    msg = input('>>')

    if not msg:
        break
    if msg == '##':
        break

    s.send(msg.encode())
    data = s.recv(1024*1024)
    print(f'receive data:{data.decode()}')

s.close()