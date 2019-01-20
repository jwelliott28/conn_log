import os

router   = "67.129.234.227"
hostname = "google.com"
hostname_response = os.system("ping -c 1 " + hostname)
router_response = os.system("ping -c 1" + router)

if hostname_response == 0:
	print hostname, 'is up!'
else:
	print hostname, 'is down!'

if router_response == 0:
	print router, 'is up!'
else:
	print router, 'is down!'
