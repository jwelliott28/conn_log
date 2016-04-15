import urllib2
import datetime
import socket

def internet_on():
    try:
        response=urllib2.urlopen('http://google.com',timeout=3)
    #    return True
    except (urllib2.URLError, socket.timeout, KeyboardInterrupt):	
        return False

file_name = 'Connection_Log_' + str(datetime.date.today()) + '.txt'

todays_log = open(file_name, 'a')

current_time = datetime.datetime.now()

#todays_log.write('Today\'s Log' + '\n' + 'Today\'s Log') 

if internet_on() == False:

    todays_log.write('Connection Lost: ' + current_time.strftime('%I:%M %p') + '\n')

todays_log.close()
