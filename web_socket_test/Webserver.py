#coding:utf-8
#与浏览器交互的WebServer
#支持中文


import socket
httpheader = """HTTP/1.1 200 OK
Content-Type: text/html;charset=utf-8
Connection:Keep-Alive

"""

host = ('127.0.0.1', 8787)
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	s.bind(host)
	s.listen(5)
except Exception,e:
	print e

while True:
	print 'listening...'
	try:
		conn,addr = s.accept()	
	except KeyboardInterrupt:
		exit(0)
	print 'Received data from: ',addr
	print conn.recv(1024)
	conn.send(httpheader +  u'中文'.encode('utf-8'))
	conn.close()
