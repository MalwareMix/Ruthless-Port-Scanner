#!/usr/bin/python
print " |====================================================================|"
print " |                          BY MALWARE MIX                            | "
print " |                      RUTHLESS PORT SCANNER                         | "
print " |              ENTER IP BELOW AND PORT YOU WANNA TEST FOR            | "
print " |====================================================================|"

import socket
ip = raw_input("Enter The IP Adress: ")
port = input("Enter Port Number: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if sock.connect_ex((ip, port)):
        print "Port", port, "is closed"
else: 
        print "Port", port, "OPEN"