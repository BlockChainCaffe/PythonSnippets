"""
Simple Asynchronous socket client experiment
"""

import socket
import sys
import select


default_port = 9999
buff_size = 1024

def check_params():
    if len(sys.argv) < 2 :
        print("not enought parameters")
        exit(-1)
    if len(sys.argv) == 2 :
        sys.argv.append(default_port)

def main():
    # create a UDP socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    check_params()
    # get local machine name
    host = sys.argv[1]
    port = int(sys.argv[2])

    # connection to hostname on the port.
    sock.connect((host, port))

    fd_in=[sock, sys.stdin]

    running = True
    print ("> ", end="")
    while running:

        read, write, error = select.select (fd_in, [sock], [sock], 3.0)

        # select returned socket ready for reading
        for s in read :
            if s == sock :
                # Receive no more than 1024 bytes from server
                msg, address = sock.recvfrom(buff_size)
                print (msg.decode('ascii'))
                if not msg :
                    print ("Server Error.")
                    running = False
            elif s == sys.stdin:
                # read the keyboard and send it
                msg = sys.stdin.readline()
                sock.sendto(str.encode(msg), (host,port))
                print ("> ", end="")
                if msg[:4] == "exit" :
                    running = False

        # select returned socket ready for writing
        for s in write :
            pass

        for s in error :
            if s is sock :
                print ("server disconnected?")
                running = False

    sock.close()



if __name__ == "__main__":
        main()
