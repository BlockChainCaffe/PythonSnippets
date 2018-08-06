"""
Simple socket client experiment
"""

import socket
import sys

default_port = 9999
buff_size = 1024

def check_params():
    if len(sys.argv) < 2 :
        print("not enought parameters")
        exit(-1)
    if len(sys.argv) == 2 :
        sys.argv.append(default_port)

def main():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    check_params()
    # get local machine name
    host = sys.argv[1]
    port = int(sys.argv[2])

    # connection to hostname on the port.
    s.connect((host, port))

    while True:
        msg = input ("> ")
        s.send(msg.encode('ascii'))
        if msg == "exit" : break
        # Receive no more than 1024 bytes
        msg = s.recv(1024)
        print (msg.decode('ascii'))

    s.close()



if __name__ == "__main__":
        main()
