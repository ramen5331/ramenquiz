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

import web
urls = (
'/input', 'index'
)
class index:
	def GET(self):
		i = web.input(name=None)
		return render.index(i.name)
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
render = web.template.render('/')