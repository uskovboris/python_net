#!/usr/bin/env python

import socket

from lib import *

UDP_IP = "xxx.xxx.xxx.xxx"

UDP_PORT = 5005

MESSAGE = to_bytes("Hello, World!")

print("UDP target IP:", UDP_IP)

print("UDP target port:", UDP_PORT)

print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes_sent = sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print("%d bytes were sent" % bytes_sent)

if bytes_sent:
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)
        print("message recieved from ", addr)

sock.close()