#!/usr/bin/env python

import socket

from lib import *

TCP_IP = '::'
TCP_PORT = 40007
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)

conn, addr = sock.accept()
print('Connection address:', addr)
while True:
    data = conn.recv(BUFFER_SIZE)

    if not data:
    	break

    print("received data:", data)
    bytes_sent = conn.send(data)
    print("%d bytes were sent" % bytes_sent)

conn.close()