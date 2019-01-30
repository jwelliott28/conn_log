#Jared Elliott
#Last Updated: 1/30/2019
#Connection_Log: Checks for internet connection and logs 
#		 a disconnect if no signal is detected

import urllib2
import datetime
import socket

#Name of the daily text log
file_name = 'Connection_Log_' + str(datetime.date.today()) + '.txt'

#Retrieves current time
current_time = datetime.datetime.now()

#Function to test for internet signal when called
#Need to edit function so that it checks/pings router first and then Google. Narrows down troubleshooting and where issue lies

def internet_on():
    try:
        response=urllib2.urlopen('http://google.com',timeout=3)
    #    return True
    except (urllib2.URLError, socket.timeout, KeyboardInterrupt):	
        return False

#If statement that calls internet_on() to see if it returns True
#Logs the time of disconnect if internet_on() is False
if internet_on() == False:

	 #Creates the daily text log
	 todays_log = open(file_name, 'a')
	 todays_log.write('Connection Lost: ' + current_time.strftime('%I:%M %p') + '\n')
	 #Saves and closes the daily text log after appending the disconnection period
	 todays_log.close()
