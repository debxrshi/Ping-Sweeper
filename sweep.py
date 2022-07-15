#!/usr/bin/python3 
 
import os

IP=input("[+] Enter the Host IP Address:\t")
print("[+] Starting Ping Sweeper on "+IP+"\n") 
dot=IP.rfind(".")
IP=IP[0:dot+1] 

"""Pings the Network"""

for i in range(1,255):
	host=IP+str(i)
	response=os.system("ping -c 1 -w 1 "+host+" >/dev/null")
	if response==0:
		print(host+" is up")
	else:
		print(host+" is down")
