#!/usr/bin/python

import socket

myname = socket.getfqdn(socket.gethostname(  ))

myaddr = socket.gethostbyname(myname)
print (myname)
print (myaddr)

import socket

myname = socket.getfqdn(socket.gethostname())
myadd = socket.gethostbyname(myname)
print(myname)
print(myadd)