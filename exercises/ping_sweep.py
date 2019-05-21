#! /usr/bin/python3
import os 

for i in range(1,254):
	resp = os.system('ping -c1 10.11.1.{}'.format(i))
	if resp == 0:
		print(' * 10.11.1.{} is up'.format(i))  
	else: 
		print('* 10.11.1.{} is down'.format(i))  

