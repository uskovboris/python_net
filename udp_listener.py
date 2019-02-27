#!/usr/bin/env python

import socket

from lib import *
    
UDP_IP = "0.0.0.0"
UDP_PORT = 5005
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print("listening to %s:%d" % (UDP_IP, UDP_PORT))
    
while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

	if data:
		print("received message: %s" % data)
		print("message recieved from ", addr)

		bytes_sent = sock.sendto(data, (addr[0], addr[1]))
		print("%d bytes were sent" % bytes_sent)
