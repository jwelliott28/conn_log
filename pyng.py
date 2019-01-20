import os
hostname = "google.com"
response = os.system("ping -c 4 " + hostname)

if response == 0:
	print hostname, 'is up!'
else:
	print hostname, 'is down!'
