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
	(c, a) = s.accept()
	l.append(c)
	print ('%d: connection from %s' % (len(l), a))
	filename = 'index.html'
    f = open(filename, 'r')

    c.sendall(str.encode("HTTP/1.0 200 OK\n",'iso-8859-1'))
    c.sendall(str.encode('Content-Type: text/html\n', 'iso-8859-1'))
    c.send(str.encode('\r\n'))
    # send data per line
    for l in f.readlines():
        print('Sent ', repr(l))
        c.sendall(str.encode(""+l+"", 'iso-8859-1'))
        l = f.read(1024)
    f.close()
    c.close()