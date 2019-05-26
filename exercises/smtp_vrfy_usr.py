#!/usr/bin/python3 
import socket
import sys
if len(sys.argv) != 3:
	print("Usage: vrfy.py <host> <username>")
	sys.exit(0)

host = sys.argv[1]
users = sys.argv[2]

f = open(users,'r')
users = f.readlines()

print('>> Scanning {}'.format(host))

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server 

connect = s.connect((host, 25))

# Recive the banner 
banner = s.recv(1024)
print(banner) 


# VRFY User

for u in users:
	u =  u.strip()
	s.send('VRFY {} \r\n '.format(u).encode())
	result = s.recv(1024)
	print(result)

# close the socket
s.close()
f.close()
