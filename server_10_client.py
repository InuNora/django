import socket
import asyncore
import threading

def myreceive(sock, msglen):
    msg = ''
    while len(msg) < msglen:
        chunk = sock.recv(msglen-len(msg))
        if chunk == '':
            raise RuntimeError("broken")
        msg = msg + chunk
    return msg
    
def  server(conn, addr):
    while True:
        data = conn.recv(1024)
        #data = myreceive(s, 1024)
        if not data: break
        conn.send(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    print("Connection", addr)
    t = threading.Thread(target=server, args=(conn, addr))
    t.start()
    
    conn.close()
    
