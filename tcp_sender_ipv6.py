#!/usr/bin/env python

import socket

from lib import *

TCP_IP = "xxxx::xxxx:xxxx:xxxx:xxxx%m"

TCP_PORT = 40007

MESSAGE = to_bytes("Hello, World!")

BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

bytes_sent = sock.send(MESSAGE)
print("%d bytes were sent" % bytes_sent)

if bytes_sent:
	data = sock.recv(BUFFER_SIZE)

sock.close()
 
print("received data:", data)