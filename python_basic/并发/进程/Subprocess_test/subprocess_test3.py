import os
import threading
import socket
import subprocess


M = threading.Lock()

OPEN = 1

HTTPHEADER = """HTTP/1.1 200 OK
Content-Type: text/html;charset=utf-8
Connection:Keep-Alive

"""


def react(conn,cli):
    global OPEN
    M.acquire()
    data = conn.recv(1024)
    if 'favicon' in data:
        conn.close()
        M.release()
        return 0
    else:
        print 'received from: ',cli
        print data
    M.release()
    conn.send(HTTPHEADER+'ok'+str(cli))
    conn.close()
    print OPEN
    if OPEN < 2:
        OPEN += 1
        subprocess.call('python test_file.py')
        print ('started')





addr = ('127.0.0.1',11116)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(5)
while True:
    conn,cli = s.accept()
    t = threading.Thread(target=react,args=(conn,cli))
    t.setDaemon(True)
    t.start()