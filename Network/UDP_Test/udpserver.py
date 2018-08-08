"""
Asynchronous socket server experiment
"""
import socket
import sys
import time

# default values
default_port = 9999
buff_size = 1024
#set of client addresses
clients = set()

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def check_params():
    if len(sys.argv) < 1 :
        print("not enought parameters")
        exit(-1)
    if len(sys.argv) == 1 :
        sys.argv.append(default_port)

def main() :
    # get local machine name
    host = ""
    port = int(sys.argv[1])
    # bind to the port
    serversocket.bind((host, port))

    # Main loop
    while True:
        data, address = serversocket.recvfrom(buff_size)
        clients.add(address)
        #print("address: {}  - data: {} ".format(address,data))
        for c in clients :
            #print("c: {} - port: {} - data: {}".format(c,port,data))
            serversocket.sendto(data,c)

    serversocket.close()


if __name__ == "__main__":
    check_params()
    main()
