'''
Allows just one instance of a program to run, 
following instances will not be allowed
Does not run on Windows (but, who cares?)
'''


## Lockin its own file

import os
import sys
import fcntl
fh=0
def run_once():
    global fh
    fh=open(os.path.realpath(__file__),'r')
    try:
        fcntl.flock(fh,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except:
        os._exit(0)

run_once()



## Using a UNIX socket

try:
    import socket
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    ## Create an abstract socket, by prefixing it with null. 
    s.bind( '\0postconnect_gateway_notify_lock') 
except socket.error as e:
    error_code = e.args[0]
    error_string = e.args[1]
    print "Process already running (%d:%s ). Exiting" % ( error_code, error_string) 
    sys.exit (0) 
