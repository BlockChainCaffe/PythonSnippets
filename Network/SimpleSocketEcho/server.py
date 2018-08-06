"""
Simple socket server experiment
"""
import socket
import sys

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
default_port = 9999
max_con = 1
buff_size = 1024

def check_params():
    if len(sys.argv) < 1 :
        print("not enought parameters")
        exit(-1)
    if len(sys.argv) == 1 :
        sys.argv.append(default_port)

def main() :

    check_params()
    # get local machine name
    #host = socket.gethostname()
    host = ""
    port = int(sys.argv[1])
    # bind to the port
    serversocket.bind((host, port))
    # queue up to 5 requests
    serversocket.listen(max_con)

    # establish a connection
    clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))

    while True:
        msg = clientsocket.recv(buff_size)
        msg1 = msg.decode('ascii')
        print ("received : {} ", format(msg))
        if msg1 == "exit": break
        clientsocket.send(msg)

    clientsocket.close()
    serversocket.close()


if __name__ == "__main__":
        main()
