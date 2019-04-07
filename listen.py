#!/usr/bin/python
import socket
import sys
import os

if (len(sys.argv) != 2 or not sys.argv[1].isdigit()):
	p = int(os.environ.get("PORT", 17995)) # get default heroku port
else:
	p = int(sys.argv[1])	

print ('Listening at port', p)

l = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', p))
s.listen(5)

while 1:
	conn, (c, a) = s.accept()
	l.append(c)
	print ('%d: connection from %s' % (len(l), a))
	filename = 'index.html'
	conn.recv(1000)
	f = open(filename, 'r')
	conn.sendall(str.encode("HTTP/1.1 200 OK\n",'ascii'))
	conn.sendall(str.encode('Content-Type: text/html\n', 'ascii'))
	conn.send(str.encode('\r\n'))
	# send data per line
	for l in f.readlines():
		print('Sent ', repr(l))
		conn.sendall(str.encode(""+l+"", 'ascii'))
		l = f.read(1024)
	f.close()
	conn.close()