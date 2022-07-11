#!/usr/bin/python3 

import os

print("[+] Input format: XXX.XXX.X.X \n")
IP=input()
print("\n[+] Running ping sweeper on "+ IP+"\n")
IP=IP[:10]
for i in range(1,255):
	host=IP+str(i)
	response=os.system("ping -c 1 -w 1 "+host+" >/dev/null")
	if response==0:
		print(host+" is up")
	else:
		print(host+" is down")
