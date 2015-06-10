import socket
import sys
import time

"""Quick little script to test fetching data every second from the server plugin"""

HOST, PORT = "localhost", 18149
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#have AC open first...
while (True):
    #ctrl-c to exit
    data = "req\n"
    sock.sendto(data.encode(), (HOST, PORT))
    received = sock.recv(1024)
    print ("Received: {}".format(received.decode()))
    time.sleep(1)
