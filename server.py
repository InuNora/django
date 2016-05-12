import socket
import asyncore

def  server(conn, addr):
    while True:
        data = conn.recv(1024)
        #data = myreceive(s, 1024)
        if not data: break
        if data == 'close': break
        conn.send(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    server(conn, addr)
    conn.close()
