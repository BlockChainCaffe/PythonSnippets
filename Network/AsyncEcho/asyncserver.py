"""
Asynchronous socket server experiment
"""
import socket
import select
import sys
import time

# default values
default_port = 9999
max_con = 1
buff_size = 1024

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setblocking(0)

# list of client sockets
sockets_in=[]
sockets_out=[]

# buffers
buffer=[]

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
    # queue up to 5 requests
    serversocket.listen(max_con)
    # add main socket to list
    sockets_in.append(serversocket)

    # Main loop
    while True:
        read, write, error = select.select (sockets_in, sockets_out, sockets_in, 3.0)

        # select returned socket ready for reading
        for s in read :
            # if is the main server socket -> new client
            if s is serversocket :
                # establish a connection
                clientsocket,addr = serversocket.accept()
                print("Got a new connection from %s" % str(addr))
                sockets_in.append(clientsocket)
                sockets_out.append(clientsocket)
                i=sockets_out.index(clientsocket)
                buffer.insert(i,[])
            else:
                # read data from this client
                msg = s.recv(buff_size)
                msg1 = msg.decode('ascii')
                print ("received : {} ", format(msg))
                if msg1[:4] == "exit" or not msg :
                    print("Closing down {}".format(s))
                    buffer.remove( buffer[sockets_out.index(s)] )
                    sockets_in.remove(s)
                    sockets_out.remove(s)
                    s.close()
                else :
                    for b in sockets_out :
                        if b != s or len(sockets_out)==1 :
                            i = sockets_out.index(b)
                            print("adding {} to {} ".format(msg,i))
                            buffer[i].append(msg)

        # select returned socket ready for writing
        for s in write :
            if s is serversocket : continue
            if s in sockets_out:
                i = sockets_out.index(s)
                #print ("S is {}, index {}".format(s,i))
                if len(buffer[i]) == 0 : continue
                print ("could write to socket {} this: {}".format(i,buffer[i][0]) )
                s.send(buffer[i][0])
                buffer[i].remove(buffer[i][0])

        for s in error :
            pass

        time.sleep(1)


    clientsocket.close()
    serversocket.close()


if __name__ == "__main__":
    check_params()
    main()
